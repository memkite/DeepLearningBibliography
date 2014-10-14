import codecs
fh = codecs.open('rawdata.txt', "rb", encoding="utf-8")
outfh = codecs.open('rawdata.bib', "wb", encoding="utf-8")

title_next=False
author_next=False
abstract_next=False

raw_title = u""
raw_authors = u""
raw_abstract = u""

for line in fh:
    if line.startswith("\n"):
#        print "#", line.strip()
        abstract_next=False 
        author_next = False
        title_next = True
        raw_title = u""
        raw_authors = u""
        raw_abstract = u""
        continue

    if title_next:
        title_next = False
        raw_title = line.strip()
        author_next = True
        continue

    if author_next:
        author_next=False
        raw_authors = line.strip()
        continue
        
    if abstract_next:
        raw_abstract = raw_abstract + " " + line.strip()
        continue

    if len(raw_authors) > 0 and len(raw_title) > 0:
        raw_title = raw_title.replace("[PDF]","").strip()
        raw_title = raw_title.replace("[DOC]", "").strip()
        raw_title = raw_title.replace("[HTML]", "").strip()

        raw_authors = raw_authors.split(" - ")[0].strip()

        print >> outfh,  "@misc{" # + id
        print >> outfh,  '  "title": "%s",' % (raw_title.replace('"'," "))
        print >> outfh,  '  "author": "%s"' % (raw_authors.replace('"'," "))
        print >> outfh,  '  "abstract": "%s"' % (raw_abstract.replace('"'," "))
        print >> outfh,  '}'
        raw_title = u""
        raw_authors = u""
        raw_abstract = u""
    
