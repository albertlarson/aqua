import requests 
from tqdm import tqdm

URL = "https://www.seanoe.org/data/00412/52367/data/86442.tar.gz"

def get_size(url):
    response = requests.head(url)
    size = int(response.headers['Content-Length'])
    return size

def download_file(url):
    local_filename = "86442.tar.gz"
    total_size = get_size(url) # total size in bytes
    chunk_size = 100000000 # size of 1 chunk to download 100000000 = 100 MB
    
    with requests.get(url, stream=True, allow_redirects=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in tqdm(r.iter_content(chunk_size = chunk_size), total  = total_size // chunk_size): # Download a 100 mb chunk
                #if chunk: 
                f.write(chunk)
    return local_filename


download_file(URL)