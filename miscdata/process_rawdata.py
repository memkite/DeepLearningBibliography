# -*- coding: utf-8 -*-

import codecs
fh = codecs.open('rawdata.txt', "rb", encoding="utf-8")
outfh = codecs.open('rawdata.bib', "wb", encoding="utf-8")

title_next=False
author_next=False
abstract_next=False

raw_title = u""
raw_authors = u""
raw_abstract = u""

title_dict = {}
id_dict = {}

keywords = {"3d":"","algorithm":"","applications":"","architecture":"","asynchronous":"","autoencoder":"","auto-encoder":"autoencoder", "adversarial nets":"adversarial networks", "adversarial network":"adversarial networks", "adversarial networks":"adversarial networks",
            "big data":"", "bioinformatics":"", "brain":"", "brain waves":"", "challenges":"", "convolutional network":"","gesture":"gesture recognition",
            "convolutional neural network":"", "deep neural network":"","deep belief network":"", "eeg":"", "emotion":"", "emotion detection":"", 
            "energy efficiency":"", "energy efficient":"", "eye tracking":"", "neuron":"","statistical inference":"","frequency domain":"",
            "face detection":"", "face recognition":"", "feature extraction":"", "finance":"", "games":"", "gpu":"", "hardware":"", "parameter":"parameters", "parameters":"parameters",
            "healthcare":"", "image recognition":"", "information retrieval":"", "infrastructure":"", "kernel methods":"", 
            "machine translation":"", "medicine":"", "memristor":"", "mine detection":"", "mobile":"", "motion detection":"", "language models":"natural language processing", "multicore":"", 
            "natural language processing":"", "neuromorphic":"", "noise":"", "noisy data":"", "online learning":"","overview":"", "parallelization":"", 
            "part-of-speech":"", "spoken language":"speech recognition", "performance improvement":"", "physics":"", "platform":"", "recommender systems":"", "regularization":"", 
            "reinforcement learning":"", "restricted boltzmann machines":"", "restricted boltzmann machine":"restricted boltzmann machines", "robotics":"", "robot":"robotics", "search":"", "sentiment analysis":"", "strategies":"",
            "simulation":"", "sparseness":"", "speech recognition":"", "stochastic gradient":"", "stochastic gradient descent":"", 
            "survey":"", "time series":"", "voice recognition":"", "sequence learning":"", "fault tolerance":"", "fault tolerant":"reliability", "reliable":"reliability", "robustness":"reliability", "acoustics":"sound", "proteins":"proteinomics", "boosting":"", "back-propagation":"back propagation", "back propagation":"", "transfer learning":"","unsupervised":"unsupervised learning", "object localization":"", "segmentation":"", "disambiguation":"", "similarity learning":"", "bayesian":"", "semantics":"", "sentiment":"sentiment analysis"}

for line in fh:
    if line.startswith("\n"):
#        print "#":"", line.strip()
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

        title_words = raw_title.split(" ")
        for i,word in enumerate(title_words):
            if word.isupper():
                title_words[i] = word.capitalize()
        raw_title = u" ".join(title_words)

        # TODO: dup 
        if not title_dict.has_key(raw_title.lower()):
            title_dict[raw_title.lower()] = True
            raw_authors = raw_authors.split(" - ")[0].strip()

            paper_id = "2015%s" % raw_authors.replace(" ", "")
            paper_id = paper_id.replace(",","")
            paper_id = paper_id.replace(".","")
            paper_id = paper_id.replace(u"…","")
            paper_id = paper_id.replace("'","")
            paper_id = paper_id.replace("_","")
            paper_id = paper_id.replace("-","")

            if not id_dict.has_key(paper_id):
                id_dict[paper_id] = raw_title
            else:
                print "COLLISSION!", paper_id ,raw_title
                paper_id = paper_id + "".join(raw_title.split(' ')[:3])
                print "NEW ID = ", paper_id
                id_dict[paper_id] = raw_title

            raw_authors = raw_authors.replace(u"…","")

            kwds = []

            for kwd in keywords:
                if kwd in raw_title.lower():
                    kwds.append(kwd)

            #if len(kwds) > 1:
            #    print kwds

            print >> outfh,  "@misc{%s," % (paper_id) # + id
            print >> outfh,  '  title = "%s",' % (raw_title.replace('"'," "))
            print >> outfh,  '  author = "%s",' % (raw_authors.replace('"'," "))
            #print >> outfh,  '  "abstract": "%s",' % (raw_abstract.replace('"'," "))
            print >> outfh,  '  keywords = {%s},' % (",".join(kwds))
            print >> outfh,  '}\n'
            raw_title = u""
            raw_authors = u""
            raw_abstract = u""
    
