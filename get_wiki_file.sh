mkdir -p wiki_dumps

dowload_folder=/home/wikipedia_dumps
mkdir -p $dowload_folder

# Portuguese Wikipedia dump from April 1, 2026, containing pages with IDs from 2207376 to 5177376
wget -P $dowload_folder https://dumps.wikimedia.org/other/mediawiki_content_current/ptwiki/2026-04-01/xml/bzip2/ptwiki-2026-04-01-p220p5177376.xml.bz2

# Spanish Wikipedia dump from April 1, 2026, containing pages with IDs from 5 to 5112706
wget -P $dowload_folder https://dumps.wikimedia.org/other/mediawiki_content_current/eswiki/2026-04-01/xml/bzip2/eswiki-2026-04-01-p5p5112706.xml.bz2

# English wikipedia
wget -P $dowload_folder https://dumps.wikimedia.org/other/mediawiki_content_current/enwiki/2026-04-01/xml/bzip2/enwiki-2026-04-01-p10p1141529.xml.bz2

# French wikipedia
wget -P $dowload_folder https://dumps.wikimedia.org/other/mediawiki_content_current/frwiki/2026-04-01/xml/bzip2/frwiki-2026-04-01-p3p3466457.xml.bz2