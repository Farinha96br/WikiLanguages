import bz2
import xml.etree.ElementTree as ET
import numpy as np

DUMP = "wiki_dumps/ptwiki-2026-04-01-p220p5177376.xml.bz2"
OUTPUT_NPY = "pt_50k.npy"




NS = "{http://www.mediawiki.org/xml/export-0.11/}"

EXCLUDED_PREFIXES = np.array(["Ficheiro:", "Imagem:", "File:", "Categoria:"])
BASE_URL = "https://pt.wikipedia.org/wiki/"
MAX_PAGES = 100_000


def extract_link_urls(text):
    parts = np.array(text.split("[["))
    parts = parts[np.char.find(parts, "]]") >= 0]
    if parts.size == 0:
        return np.array([], dtype="U1")
    get_title = np.vectorize(lambda p: p.split("]]")[0].split("|")[0].strip())
    titles = get_title(parts)
    is_excluded = np.zeros(titles.size, dtype=bool)
    for prefix in EXCLUDED_PREFIXES:
        is_excluded |= np.char.startswith(titles, prefix)
    titles = titles[~is_excluded]
    if titles.size == 0:
        return np.array([], dtype="U1")
    return np.char.add(BASE_URL, np.char.replace(titles, " ", "_"))


# Pre-allocate a 2D (MAX_PAGES x 2) object array: col 0 = title, col 1 = num_links
arr = np.empty((MAX_PAGES, 2), dtype=object)
count = 0

with bz2.open(DUMP, "rb") as f:
    for event, elem in ET.iterparse(f, events=("end",)):
        if elem.tag != f"{NS}page":
            continue

        if elem.findtext(f"{NS}ns") != "0":
            elem.clear()
            continue

        title = elem.findtext(f"{NS}title")
        text = elem.findtext(f".//{NS}text") or ""

        arr[count, 0] = title
        arr[count, 1] = extract_link_urls(text).size

        elem.clear()
        count += 1
        if count % 10_000 == 0:
            print(f"{count} pages processed...")
            print("current page:", title)
        if count >= MAX_PAGES:
            break

arr = arr[:count]
np.save(OUTPUT_NPY, arr)
print(arr[0])
print(f"Saved shape {arr.shape} to {OUTPUT_NPY}")
