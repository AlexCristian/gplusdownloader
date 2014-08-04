#!/usr/bin/env python
import urllib2
import urllib
import os

""" gplusdownloader.py: Downloads an entire Google Plus or Picasa album onto your disk  """

__author__ = "Alexandru Cristian"

ALBUM_URL = ""
IMAGE_TOKEN = "IMG_"
IMAGE_EXTENSION = ".JPG"
IMAGE_URL_BGN = "https://"
SAVE_PATH = "gplus_images/"
DEBUG = False

RESOLUTION_SUFFIX = "/w9999"
downloaded_filenames = []

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

response = urllib2.urlopen(ALBUM_URL)
html = response.read()

pos=html.find(IMAGE_TOKEN)
pic_counter = 0
while pos != -1:
    if  html[:pos].rfind(IMAGE_URL_BGN) != -1:
        start = html[:pos].rfind(IMAGE_URL_BGN)
        extension_pos = html[pos:].find(IMAGE_EXTENSION.upper())
        if extension_pos > html[pos:].find(IMAGE_EXTENSION.lower()):
            extension_pos = html[pos:].find(IMAGE_EXTENSION.lower())
        end = pos + extension_pos + len(IMAGE_EXTENSION)
        download_url =  html[start:end]
        
        filename = download_url[download_url.rfind("/"):]
        download_url = download_url[:download_url[:download_url.find(filename)].rfind("/")]
        download_url = download_url + RESOLUTION_SUFFIX + filename
        
        if filename not in downloaded_filenames and '"' not in download_url:
            downloaded_filenames.append(filename)
            print "Getting " + download_url + " (%d)" % (pic_counter+1)
            urllib.urlretrieve(download_url, SAVE_PATH + filename)
            pic_counter += 1
        
    html = html[pos+1:]
    pos=html.find(IMAGE_TOKEN)   
    if DEBUG == True:
        break
print "DONE: Downloaded %d images." % pic_counter
