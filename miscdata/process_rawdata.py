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

# new ones
new_keywords = {"photonic":"photonic", "clustering":"clustering", "classification":"classification","regression":"regression",
                "coding scheme":"coding scheme","spatial":"spatial", "spatially":"spatial", "depression":"healtchare","svm":"svm","estimation":"estimation","estimate":"estimation",
                "deep sigmoid belief networks":"deep belief networks", "sigmoid":"sigmoid","cell":"bioinformatics","stochastic":"stochastic","cognitive":"", "cognition":"cognitive",
                "information theoretic":"", "information-theoretic":"information theoretic","acoustic":"", "phoneme":"", "blood":"healthcare","sign language":"", "image classification":"", "sparse":"sparsity", "sparsity":"", "gradient":"gradient", "features":"feature extraction", "cloud":"", "data-parallel":"parallel", "dictionary extraction":"",
                "bird":"biology", "data mining":"data mining", "sound retrieval":"sound", "vocal":"sound", "handwritten":"", "character recognition":"", "object recognition":"",
                "fine tuning":"", "fine-tuning":"", "action recognition":"", "acoustic model":"acoustic", "weather prediction":"meteorology", "weather forecast":"meteorology",
                "meteorology":"", "planning":"", "pre-training":"", "content-based":"content based", "content based":"", "hierarchical":"",
                "lfw":"face recognition", "feature":"feature representation", "features":"feature representation", "visual":"", "controller":"",
                "visual memory":"", "dnn":"deep neural networks", "cnn":"convolutional neural networks", "rbm":"restricted boltzmann machines",
                "sda":"stacked denoising autoencoders", "lstm":"long short term memory", "rnn":"recurrent neural network", "rntn":"recursive neural tensor network",
                "traffic sign":"traffic sign recognition", "endocrinology":"medicine", "transductive":"", "stochastic optimization":"",
                "depth-videos":"video", "videos":"video", "feature encoding":"feature representation", "fuzzy learning":"", "semi-supervised":"",
                "semi supervised":"semi-supervised", "pedestrian detection":"", "gradient":"", "behavior model":"behavior model", "behavior modelling":"behavior model",
                "behavior models":"behavior model", "decision making":"", "traffic":"traffic", "video":"video", "entities":"entity", "entity":"",
                "2d":"", "3d":"", "speech":"speech recognition", "term":"natural language processing", "deep belief nets":"deep belief networks",
                "scene recognition":"", "representation learning":"", "spectral":"", "hyperspectral":"spectral", "activity detection":"",
                "long short-term memory":"long short term memory", "speech":"speech recognition", "speech synthesis":"speech synthesis",
                "noisy":"noise","human pose":"pose recognition", "invariant":"", "temporal":"", "imagery":"image",
                "hashing":"", "kernel":"", "transfer learning":"", "imaging":"image", "support vector machine":"support vector machines", "support vector machines":"",
                "constrained":"", "convolutional":"convolutional neural networks", "representation learning":"", "embedded":"", "optimized":"optimization",
                "summarization":"", "graphical model":"", "hashing":"", "hash":"hashing", "aircraft detection":"", "gaussian":"",
                "sar data":"synthetic aperture radar data", "latent structure":"", "fmri":"medicine", "freehand":"", "scene classification":"",
                "sketch recognition":"", "theory":"", "proof":"theory", "active learning":"", "review":"survey", "study":"survey",
                "estimation":"", "supervised":"supervised learning", "face":"face recognition",
                "monte carlo":"", "hand pose":"hand pose recognition", "vowel":"natural language processing",
                "belief propagation networks":"", "vehicle":"", "subspace analysis":"", "dropout":"", "batchwise":"batch", "batch":"",
                "alzheimer's":"medicine", "hmax":"", "dcnn":"convolutional neural networks", "rectifiers":"rectifier function",
                "rectifiers:":"rectifier function", "human-level":"", "human level":"human-level",
                "quantum":"", "road detection", "linear model":"linear models", "linear models":"", "scheduling":"",
                "event":"", "feature selection":"feature representation", "web search":"search",
                "occlusions":"", "occlusion":"occlusions", "calibration":"", "dataset":"", "medical":"medicine", "corpora":"natural language processing",
                "traffic prediction":"", "random fields":"", "random field":"", "gradient-based":"gradient",
                "optimization":"", "batch normalization":"", "perceptron":"", "over-sampling":"sampling",
                "sensor data":"", "denoising":"noise", "multi-label":"", "missing":"sparsity", "big":"big data",
                "social":"", "human behavior", "sensor data":"", "hessian":"", "newton":"", "pose":"pose detection",
                "genetic programming":"", "biologically":"biology", "discriminative":"",
                "demodulation":"", "error correction":"", "non-convex":"", "non convex":"non-convex",
                "weld":"welding", "welding":"", "collaborative filtering":"recommender systems",
                "numerical":"", "sensory":"sensory data", "neuroscience":"brain", "recurrent":"recurrent neural network",
                "adaptive":"", "hmm-based":"hidden markov model", "speech synthesis":"",
                "framework":"", "computer vision":"image recognition", "personalize":"personalization", "personalization":"",
                "autonomous":"", "autonomously":"autonomous", "rectified":"rectifier function",
                "robust":"", "disease":"medicine", "event":"", "generative":"", "convnet":"convolutional neural networks",
                "convnets":"convolutional neural networks", "transcription":"", "dictionary":"natural language processing",
                "softmax":"", "fpga-based":"hardware","fpga":"hardware", "energy":"", "diacritization":"natural language processing",
                "semantic":"", "features":"feature representation", "tree structures":"algorithms", "tree structure":"algorithms",
                "cascade":"cascading", "cascading":"", "motion":"", "concept learning":"", "blstm":"long short term memory",
                "recurrent nets":"recurrent neural network", "spatio-temporal":"", "distributed":"", "advertising":"","ads":"advertising",
                "articulatory synthesis":"speech synthesis", "facial":"face recognition", "action selection":"",
                "clustered":"clustering", "drug":"medicine", "ensemble learning":"", "astronomy":"",
                "word-sense":"natural language processing", "word sense":"natural language processing",
                "kernels":"kernel", "parsing":"natural language processing", "click-through":"human behavior",
                "clickthrough":"human behavior", "click through":"human behavior", "thermodynamics":"",
                "predicting":"prediction", "prediction":"", "logistic":"", "feature discovery":"feature representation",
                "boosted":"boosting", "network congestion":"", "processor":"hardware", "mimd":"hardware", "big-data":"big data",
                "smart city":"", "network analysis":"", "semantic hashing":"", "semantic indexing":"", "ct":"medicine",
                "pancreas":"medicine", "user interface":"", "user interfaces":"", "predictors":"prediction",
                "plankton":"biology", "approximate":"approximation", "lasso":"", "recommendation systems":"recommender systems",
                "word embeddings":"natural language processing", "galaxy":"astronomy", "feature":"feature representation",
                "hash":"hashing", "mri":"medicine", "shape classification":"", 
                
                
}

keywords.update(new_keywords)                

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
    
