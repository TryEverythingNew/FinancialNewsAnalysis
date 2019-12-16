# Course Project 

Financial News Analysis
- Group: (only one person)
- Person1: xueliang sun, xs23, xs23@illinois.edu

## Overview

This software supports:

- Download financial news of wanted stocks
- Extract key features for sentiment analysis
- Classify whether the news is good or bad

## Assumptions

This software assumes you already install python3, BeautifulSoup, MetaPy, Selenium.

## Usage 1: Download News

Step 1: modify the text file to write down your interested stock symbols

- cd scraper_code/
- vi wanted_stock_symbols.txt
- python scraper.py

The symbols you provide, should be tradable.
The content of news will be saved to news.txt and you can manually view them.


