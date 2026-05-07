import os
import re
import subprocess
import urllib.request
from urllib.parse import urljoin
from utils.etc import cprint

wiki_folder = '/home/farinha/wiki/'
wiki_lists = ['ptwiki', 'eswiki', 'dewiki', 'frwiki', 'itwiki', 'ruwiki', 'jawiki', 'kowiki', 'zhwiki']
latest_date = "2026-05-01"

def final_url(wiki, date):
    tmp = 'https://dumps.wikimedia.org/other/mediawiki_content_current/'
    tmp += wiki + '/' + date + '/xml/bzip2/'
    return tmp

def list_remote_files(url):
    """Returns list of .bz2 URLs if _SUCCESS exists on the directory page, else None."""
    with urllib.request.urlopen(url) as resp:
        html = resp.read().decode('utf-8')

    hrefs = re.findall(r'href="([^"]+)"', html)

    if any('_SUCCESS' in h for h in hrefs):
        cprint("  _SUCCESS found, files are valid", 'green')
        print(f"  Found {len(hrefs)} links, filtering for .bz2...")
        
        return [urljoin(url, h) for h in hrefs if h.endswith('.bz2')]
    else:
        cprint("  _SUCCESS not found, skipping", 'red')
        return None
    


# list all the remote files
for wiki in wiki_lists:
    url = final_url(wiki, latest_date)
    files = list_remote_files(url)



#for wiki in wiki_lists:
#    url = final_url(wiki, latest_date)
#    print(f"\nChecking {wiki}: {url}")
#
#    try:
#        files = check_and_get_files(url)
#        if files is None:
#            print(f"  _SUCCESS not found, skipping {wiki}")
#            continue
#
#        dest = os.path.join(wiki_folder, wiki)
#        os.makedirs(dest, exist_ok=True)
#        print(f"  Found {len(files)} .bz2 file(s), downloading to {dest}")
#
#        for file_url in files:
#            subprocess.run(['wget', '-c', '-P', dest, file_url], check=True)
#
#    except Exception as e:
#        print(f"  Error processing {wiki}: {e}")
