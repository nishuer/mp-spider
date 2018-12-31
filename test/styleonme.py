import os
from app.api import request
from bs4 import BeautifulSoup
import re
import time
import urllib.request

def writeId(fileName, id):
	with open('%s/app/data/image_id/id_%s_data.txt' % (os.getcwd(), fileName), 'a', encoding='utf8') as f:
		f.write('%s\n' % url)

def readId(fileName, id):
	with open('%s/app/data/image_id/id_%s_data.txt' % (os.getcwd(), fileName), 'r', encoding='utf8') as f:
		try:
			f.readlines().index('%s\n' % id)
			return True
		except ValueError:
			return False

def mkdir(path):
	folder = os.path.exists(path)

	if not folder:
		os.mkdir(path)
	else:
		print('Folder already exists')

	return path

def getTimeStr():
	return time.strftime("%H%M%S", time.localtime())

def getItemId(url):
	res = re.search(r'\d+\.?\d*', url)
	return res.group()


r = request.get('http://www.styleonme.com/items/louisangel/0119/2/')

soup = BeautifulSoup(r.text, 'lxml')

items = soup.find_all('a', href=re.compile('/items/detail'))

for item in items:
	url = item['href']

	id = getItemId(url)

	if (readId('styleonme', id)):
		break

	time.sleep(6)

	r = request.get('http://www.styleonme.com/%s' % url)

	soup = BeautifulSoup(r.text, 'lxml')

	imgs = soup.find_all('img', { 'name': 'detail_images' })

	path = mkdir('%s/images/%s' % (os.getcwd(), id))

	for index, img in enumerate(imgs):
		imgUrl = 'http:%s' % img['src']
		urllib.request.urlretrieve(imgUrl, "%s/%d.jpg" % (path, index))
		time.sleep(3)

	writeId('styleonme', id)
