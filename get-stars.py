# by cycuestaa
import os
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

# variables 
dest = "./starimgs/"    # files save here. make sure ends with /
obj_name = "M3_i-band"
file_type = "FCAL.fits"
obj_len = len(obj_name)
ft_len = len(file_type)
count = 1 

## CREATE directory, if doesnt exist
path = os.getcwd()
print("Detected working dir: %s" % path)
try:
    os.mkdir(dest)
except OSError:
    print ("CREATE failed. dir: %s likely exists" % path)
else:
    print ("CREATE done. files will save into dir: %s" % path)


## GET & Download
for a_tag in soup.findAll('a'):  #'a' tags are for links
    if count >= 6 : # line for first file listed
        link = a_tag['href']

        if(link[:obj_len]==obj_name)&(link[-ft_len:]==file_type):
            print(link)
            download_url = url + link
            urllib.request.urlretrieve(download_url,dest+link) 
            time.sleep(1) # pause to not break 

    count += 1





