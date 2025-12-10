"""
Real_world example: Multithreading for I/O-bound tasks 
Scenario: Web Scraping
Web scraping often involves making numerous network request to fetch web pages. These tasks are I/O-bound because they spend a lot of time waiting for responses from servers. Multithreading can significantly improve performance.
"""

import threading 
import requests
from bs4 import BeautifulSoup

urls = [
    'https://developers.google.com/edu/python',
    'https://developers.google.com/edu/python/introduction',
    'https://developers.google.com/edu/python/utilities'
]

def fetch_content(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f'Fetched {len(soup.text)} characters from {url}')
    except Exception as e:
        print(f'Error fetching {url}: {e}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)  # append thread, not threads
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")