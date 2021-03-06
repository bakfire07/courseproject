
"""
Scraps twitter using selenium.

This module requires selenium to be installed.
"""
import argparse
import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import urllib
import random
# set the driver
CHROMEDRIVER = "/Users/balamurali/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = CHROMEDRIVER

class TwitterCrawler():

    def __init__(self,input_file,output_file,call_type):
        self.output_file = output_file
        self.driver = webdriver.Chrome(CHROMEDRIVER)
        self.call_type = call_type
        self.data_list = self.load_input_data(input_file)


    def load_input_data (self,input_file):
        """
        load the input data to a list
        :return:
        """
        data_list = list()
        fs = open(input_file,'r')
        for line in fs:
            #data_list.append(urllib.quote_plus(line))
            data_list.append(line.strip())
        fs.close()
        return data_list

    def crawl(self):
        """
        crawl the twitter for the search items
        :return:
        """
        if self.call_type=='search':
            base_url = "https://twitter.com/search?q="
        else:
            base_url = "https://twitter.com/"
        fo = open(self.output_file,'w')
        driver = self.driver
        for search_item in self.data_list:
            print 'Searching for term:{}'.format(search_item)
            driver.get(base_url + search_item)
            # get the body of the html
            body = driver.find_element_by_tag_name('body')
            for _ in range(2):
                body.send_keys(Keys.PAGE_DOWN)
                # randomize the clicks so that twitter cannot understand it is a bot hitting
                time.sleep(random.choice(range(4,8)))

            tweets = driver.find_elements_by_class_name('tweet-text')
            for tweet in tweets:
                if len(tweet.text):
                    try:
                        fo.write("{}:#:{} \n".format(search_item,tweet.text.encode('UTF-8').replace('\n','. ')))
                    except Exception as e:
                        pass
                # sleep before the next url is hit
            time.sleep(random.choice(range(0,5)))
            fo.flush()
        fo.close()
        driver.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Program to scrap twitter.')
    parser.add_argument('-input', dest='input', help='Input file containing',required=True)
    parser.add_argument('-output', dest='output', help='Input file containing',required=True)
    parser.add_argument('-type', dest='type', help='Type can be for simple user search or complex one. If complex copy the part after https://twitter.com/',default='search')
    args = parser.parse_args()
    twitter_crawler = TwitterCrawler(args.input,args.output,args.type)
    twitter_crawler.crawl()