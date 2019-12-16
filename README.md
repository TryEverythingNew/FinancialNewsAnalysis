# Course Project 

Financial News Analysis
- Group: (only one person)
- Person1: xueliang sun, xs23, xs23@illinois.edu

## Overview

This software supports:

- Download financial news of wanted stocks
- Classify whether the news is good or bad

## Assumptions

This software assumes you already install python3, BeautifulSoup, MetaPy, Selenium.

## Usage 1: Download News

Step 1: modify the text file to write down your interested stock symbols

- cd scraper_code/
- vi wanted_stock_symbols.txt

Step 2: run python code to download
- python scraper.py

The symbols you provide, should be tradable.
The content of news will be saved to news.txt and you can manually view them.

## Usage 2: Classify News

Step 1: copy your downloaded news to another folder for test

- cp scraper_code/news_url.txt test_news/
- cp scraper_code/news.txt test_news/test_news.dat

Step 2: run python code to classify
- python analyze_news.py

## Explanation of Implementation

I studied the web format of financial news in yahoo. And then I wrote programs to download the news for interested stocks.
This part requires a lot of research on html format, BeautifulSoup usage, and selenium.
To classify news, I prepared a training data set with labels. You can find them under train_news sub-folder.
I manually did the labeling on my own. This labeled data is then used to create forward index.
And then I did many study on how to create a forward index and classifier using metapy.
By referring to many materials, I chose NaiveBayes classifier to classifier whether a news is good or bad.
The result is pretty good!
