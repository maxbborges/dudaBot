from urllib.request import urlretrieve

def download(url,fileName):
    urlretrieve(url,fileName)