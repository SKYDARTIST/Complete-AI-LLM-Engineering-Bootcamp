import threading
import requests
import time


def download(url):
    print(f"Downloading from {url}...")
    res = requests.get(url)
    print(f"Finished downloading from {url}...")


urls = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.twitter.com",
    "https://www.youtube.com",
    "https://www.linkedin.com",
    "https://www.github.com",
    "https://www.reddit.com",
    "https://www.whatsapp.com",
    "https://www.telegram.org",
]



start = time.time()

threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    threads.append(t)
    t.start()


for t in threads:
    t.join()

end = time.time()

print(f"Total time for downloading {len(urls)} URLs is {end-start:.2f} seconds")