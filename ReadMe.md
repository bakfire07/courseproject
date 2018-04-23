PROGRAM TO CRAWL TWITTER

BASIC TEXT PROCESSING HELPER CLASS

This is a helper class to process text. To execute the same please follow the instructions

1. Install the dependencies by doing
pip install -r requirements.txt

python -m textblob.download_corpora

2. Execute helper.py

python helper.py --input

parameter specification

-input -  text file containing tweets/text to be analyzed with one instance per line
-p     -  get the pos tag associated with each instance
-s     -  get the overall sentiment
-ss    -  get the sentence sentiment
-n     -  get the noun phrase
-ner   -  get the NER tags of the instance
-po    -  get the POS tags of the instance
-t     -  tokenize the instance and get words


3. The output is saved in a json format : out.json