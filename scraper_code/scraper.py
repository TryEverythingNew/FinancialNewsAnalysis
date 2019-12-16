from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import os
import re 
import urllib.request

options = Options()
options.headless = True
browser = webdriver.Chrome( f'./chromedriver.exe',options=options)


#uses webdriver object to execute javascript code and get dynamically loaded webcontent
def get_js_soup(url,browser):
    browser.get(url)
    res_html = browser.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(res_html,'html.parser') #beautiful soup object to be used for parsing html content
    return soup

#tidies extracted text 
def clean_text(text):
    text = text.encode('ascii',errors='ignore').decode('utf-8')       #removes non-ascii characters
    text = re.sub('\s+',' ',text)       #repalces repeated whitespace characters with single space
    return text

''' More tidying
Sometimes the text extracted HTML webpage may contain javascript code and some style elements. 
This function removes script and style tags from HTML so that extracted text does not contain them.
'''
def remove_script(soup):
    for script in soup(["script", "style"]):
        script.decompose()
    return soup


def search_div_id(div_id):
    return div_id and re.search('latestQuoteNewsStream', div_id)

def search_href(href):
    return href and re.search('/news/', href)

#extracts all Faculty Profile page urls from the Directory Listing Page
def scrape_specific_stock(stock_symbol,browser):
    base_link = f'https://finance.yahoo.com/quote/{stock_symbol}/news?p={stock_symbol}'
    url_list = []
    #execute js on webpage to load the list of news for given stock
    soup = get_js_soup(base_link,browser)
    for link_holder in soup.find_all('div', id=search_div_id):
        for tag in link_holder.find_all('a', href=search_href):
            url_list.append('https://finance.yahoo.com' + tag['href'])
    url_list = sorted(set(url_list))
    print ('-'*20, f'Found {len(url_list)} urls of news for {stock_symbol}','-'*20, flush=True)
    return url_list

def write_lst(lst, file_):
    with open(file_,'w', encoding='utf-8') as f:
        for line in lst:
            f.write(line)
            f.write('\n')


url_list = []
with open('./wanted_stock_symbols.txt', 'r') as file:
    for line in file.readlines():
        stock_symbol = line.strip()
        url_list.extend( scrape_specific_stock(stock_symbol,browser))
write_lst(url_list, './news_url.txt')

news_list = []
for url in url_list:
    try:
        soup = remove_script(get_js_soup(url, browser))
        article_tag = soup.find('article')
        if article_tag is None:
            print(f"News {url} doesn't have article tag; will ignore this url", flush=True)
        else:
            content_list = [tag.get('content', '') for tag in article_tag.find_all('p')]
            news_list.append(clean_text(' '.join(content_list).replace('\n', ' ')))
    except BaseException as err:
        print(f"Met {err} for {url}", flush=True)
write_lst(news_list, './news.txt')
