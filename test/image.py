import os
from app.api import request
from bs4 import BeautifulSoup
import re
import time

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}

cookies = {
	"_cc_":	"VFC%2FuZ9ajQ%3D%3D",
	"_m_h5_tk":	"66225a49d63d7bd627e02f0d37435c19_1545677162149",
	"_m_h5_tk_enc":	"2056dd1f075e6ea85f72c859d5371878",
	"_tb_token_": "e9bde15fb93b",
	"cna":	"Se6nFPzbQSgCAXHwowy/l/zU",
	"cookie2": "1ffd6b57e970a3d277f2c25f81cb0ce9",
	"csg": "c66f9476",
	"dnk": "bonwe_pc",
	"enc": "qaVOQZqYdE6N07bJBY%2F8aYizHd6KaKeD%2Fwst8NjVeVmENLseYQgbnCh5eQbKACNpeisv9Ewd6qIW0qaX5oLMPw%3D%3D",
	"existShop": "MTU0NTcyODY4Mg%3D%3D",
	"hng": "CN%7Czh-CN%7CCNY%7C156",
	"isg": "BOzsOsVLnJ1Fe49ZoHdjKe3WvczeDZE67ddAXEYt-Rc6UYxbbrWw3wnndVnMWcin",
	"l": "aB7l9j2OysEgEe2BsMaiBX71z707gh5zlVW91MamaiThNP30pTBaUj-o-VwWj_qC5Jcy_K-5F",
	"lgc": "bonwe_pc",
	"mt": "ci=0_1&np=",
	"pnm_cku822": "098%23E1hvqQvUvbpvUvCkvvvvvjiPR25wsj3CRLMhQj3mPmPwQjtWRsqUsji8RFzZ6jrRmphvLC2K0QvjOrjxAfyp%2B3%2B%2Ba4A%2B%2BboJaZzZtb2XrqpyCW2%2BFO7t%2BeCxTWex6fItb9TxfJCl53htcUkQD76wd56OfJCldCVDWhvH6OkQ%2Bu0tvpvIvvvvk6CvvvvvvUEpphvhqpvv9DCvpvQovvmmZhCv2bZvvUEpphvWq8yCvv9vvUmsih3XBOyCvvOUvvVCa6wCvpvVvmvvvhCv2QhvCvvvMMGtvpvhvvvvv8wCvvpvvUmm",
	"skt": "c2e2d9a7069c3ce6",
	"t": "c597a5a3d4fd3497a3b1eb5f94c1488d",
	"tg": "0",
	"thw": "cn",
	"tracknick": "bonwe_pc",
	"uc1": "cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=VT5L2FSpczFp&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTYM8HKzf%2BbsA%3D%3D&tag=8&lng=zh_CN",
	"uc3": "vt3=F8dByRMA7jHatvLUHcM%3D&id2=UoCJipcu0G8P&nk2=AQuN4XVxnCY%3D&lg2=W5iHLLyFOGW7aA%3D%3D",
	"v": "0"
}

maxPage = 0

def writeIds(fileName, ids):
	with open('%s/test/data/ids_%s_data.txt' % (os.getcwd(), fileName), 'a', encoding='utf8') as f:
		f.write('%s,' % ids)

def getIds(pageNo):
	global maxPage

	url = 'https://xiaojie.taobao.com/i/asynSearch.htm?callback=jsonp348&mid=w-19788214760-0&wid=19788214760&path=/search.htm&search=y&pageNo=%s' % pageNo

	r = request.get(url, headers=headers, cookies=cookies)

	# print(r.text)

	if (not maxPage):
		res = re.search(r'(?<=\>1\/).*?(?=\<)', r.text)
		maxPage = res.group()

	ids = re.search(r'(?<=itemIds=).*?(?=&source)', r.text)

	print(pageNo)
	print(ids.group())

	writeIds('xiaojie', ids.group())

getIds(1)

if (int(maxPage) > 1):
	for i in range(2, int(maxPage) + 1):
		time.sleep(20)
		getIds(i)
