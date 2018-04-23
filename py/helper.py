"""
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

"""
from textblob import TextBlob
import json
import argparse


def analyze_sentence_sentiment(blob):
    """
    Get the sentence level sentiment
    :param text:
    :return:
    """
    polarity = list()
    for sentence in blob.sentences:
        intensity = sentence.sentiment.polarity
        if intensity > 0:
            sentiment = 'pos'
        elif intensity < 0:
            sentiment = 'neg'
        else:
            sentiment = 'neu'
        polarity.append(sentiment)

    return polarity


def analyze_sentiment(blob):
    """
    sentence polarity is returned
    :param blob:
    :return:
    """
    intensity  = list(blob.sentiment)[0]
    if intensity > 0:
        sentiment = 'pos'
    elif intensity < 0:
        sentiment = 'neg'
    else:
        sentiment = 'neu'

    return sentiment


def get_pos_tags(blob):
    """
    get the pos tags of the sentence
    :param text:
    :return:
    """
    return blob.pos_tags


def get_noun_phrases(blob):
    """
    returns the noun phrases associated with
    :param text:
    :return:
    """
    return blob.noun_phrases


def get_parsed_text(blob):
    """
    dependency parse the text
    :param blob:blob object holding text
    :return:
    """
    return blob.parse()


def get_correct_spelling(blob):
    """
    returns correct spelling
    :param text:
    :return:
    """

    return blob.correct()


def get_tokenizer_result(blob):
    """
    get the tokenizer results
    :param blob:
    :return:
    """
    return list(blob.words)


def process_corpus(args):
    """
    process the text based on the
    :param params:
    :param input_data:
    :return:
    """

    fs = open(args.input,'r')
    out = list()
    for line in fs:
        blob = TextBlob(line.strip())
        result_info = dict()
        result_info
        result_info['correct'] = str(blob.correct())
        if args.parse :
            result_info['parse'] = get_parsed_text(blob)
        if args.tokenize:
            result_info['tokenize'] = get_tokenizer_result(blob)
        if args.sentiment:
            result_info['sentiment'] = analyze_sentiment(blob)
        if args.sentence_sentiment:
            result_info['sentence_sentiment'] = analyze_sentence_sentiment(blob)
        if args.noun_phrase:
            result_info['noun_phrase'] = get_noun_phrases(blob)
        if args.pos:
            result_info['pos'] = get_pos_tags(blob)

        out.append(result_info)
    print out
    json.dump(out,open('out.json','w'))
    fs.close()
    print '*******************************    Execution completed        *********************************'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Helper class to get the text mining going.',
                                         epilog='The output is saved in a json format : out.json')
    parser.add_argument('-p', action='store_true', dest='parse', help='get the pos tag associated with each instance')
    parser.add_argument('-s', action='store_true', dest='sentiment', help='get the overall sentiment')
    parser.add_argument('-ss', action='store_true', dest='sentence_sentiment', help='get the sentence sentiment')
    parser.add_argument('-n', action='store_true', dest='noun_phrase', help='get the noun phrase')
    parser.add_argument('-ner', action='store_true', dest='ner', help='get the NER tags of the instance')
    parser.add_argument('-po', action='store_true', dest='pos', help='get the POS tags of the instance')
    parser.add_argument('-t', action='store_true', dest='tokenize', help='tokenize the instance and get words')
    parser.add_argument('--input',  dest='input',required=True, help='text file containing tweets/text to be analyzed with one instance per line')
    # parse the arguements
    args = parser.parse_args()
    # call the driver method
    process_corpus(args)

