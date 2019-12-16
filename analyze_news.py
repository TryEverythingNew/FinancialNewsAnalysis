import metapy

train_idx = metapy.index.make_forward_index('train.toml')
train_dset = metapy.classify.MulticlassDataset(train_idx)

np = metapy.classify.NaiveBayes(train_dset)
print("classify for traning data", flush=True)
for train in train_dset:
    print(f"Actual label is {train_dset.label(train)}, classified to {np.classify(train.weights)}")

with open('test_news/news_url.txt', 'r') as file:
    url_list = file.readlines()
test_idx = metapy.index.make_forward_index('test.toml')
print("classify for test data, test data might not be labeled", flush=True)
for url, test in zip(url_list, metapy.classify.MulticlassDataset(test_idx)):
    print(f"URL {url} is classified to {np.classify(test.weights)}")
