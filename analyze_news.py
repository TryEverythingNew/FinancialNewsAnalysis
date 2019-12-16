import metapy

def count_word(doc):
    #Write a token stream that tokenizes with ICUTokenizer,
    #lowercases, removes words with less than 2 and more than 30 characters
    #performs stemming and creates trigrams (name the final call to ana.analyze as "trigrams"
    tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
    tok = metapy.analyzers.LowercaseFilter(tok)
    tok = metapy.analyzers.LengthFilter(tok, min=2, max=30)
    tok = metapy.analyzers.Porter2Filter(tok)
    tok = metapy.analyzers.ListFilter(tok, "lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)
    ana = metapy.analyzers.NGramWordAnalyzer(1, tok)
    trigrams = ana.analyze(doc)
    tok.set_content(doc.content())
    tokens, counts = [], []
    return {token: count for token, count in trigrams.items()}

train_idx = metapy.index.make_forward_index('train.toml')
with open('./scraper_code/news.txt', 'r') as file:
    news_list = [line.strip() for line in file.readlines()]
with open('./scraper_code/news_url.txt', 'r') as file:
    url_list = [line.strip() for line in file.readlines()]
assert len(url_list) == len(news_list), "The number of urls mismatchs the number of news"

for url, news in zip(url_list, news_list):
    doc = metapy.index.Document()
    doc.content(news)
    

