# Import libraries
# https://python-forum.io/Thread-Web-Scraping-part-1
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from bs4 import CData

# set url to the website
url = 'http://stars.uchicago.edu/images/StoneEdge/0.5meter/2020/2020-05-09/itzamna/'
response = requests.get(url)

# parse html
soup = BeautifulSoup(response.text, "html.parser")

# locate all <a> tags
count = 1 
url_len = len(url)

for a_tag in soup.findAll('a'):  #'a' tags are for links
    if count >= 6 : # line for first file listed
        link = a_tag['href']
#        test += 1
        print(count, link)
        download_url = url + link
        urllib.request.urlretrieve(download_url,'./imgs/'+link) 
        time.sleep(1) # pause to not break 
    count += 1





