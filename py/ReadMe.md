

## Requirements
You need to install python3 for the projects. You are free to use any other language to meet the objective. 

In case you choose python as your weapon of choice, please run the following to install all the dependencies required for running the programs mentioned in this git repo. You can use any editor to run your code. I would recommend [pycharm - community edition](https://www.jetbrains.com/pycharm/download/)

```
pip install -r requirements.txt

python -m textblob.download_corpora
```



##### Program to crawl Twitter
This program is used to crawl the twitter for keywords/search commands mentioned on the Twitter. This program uses [Selenium](https://www.seleniumhq.org), a web automation tool. To run this program you need to have chrome browser installed and the [driver path](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver) for the same added to twitter_scrapy.py code

```python
# set the driver
CHROMEDRIVER = "/Users/demo/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = CHROMEDRIVER

```
```
python twitter_scrapy.py -input twitter_sample.txt -output out.json 
```


##### Basic Text Processing class

This is a helper class to process text. To execute the same please follow the instructions


1. Execute helper.py

```
python helper.py --input
```
parameter specification

-input -  text file containing tweets/text to be analyzed with one instance per line
-p     -  get the pos tag associated with each instance
-s     -  get the overall sentiment
-ss    -  get the sentence sentiment
-n     -  get the noun phrase
-ner   -  get the NER tags of the instance
-po    -  get the POS tags of the instance
-t     -  tokenize the instance and get words


2. The output is saved in a json format : out.json
