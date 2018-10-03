from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
#params = {'search': 'Harry Potter'}
#params={'search': 'Harry'}
f=open("books.txt","r")
fi=open("newbooks.txt","w+")
f1=f.readlines()
for i in f1:
	j=i.replace(" ","+")
	search_url = 'https://www.goodreads.com/search?utf8=%E2%9C%93&q='+j+'&search_type=books'
	#url = search_url + urlencode(params)
	r = requests.get(search_url)
	soup = BeautifulSoup(r.content, 'html.parser')

	l = soup.find(class_="minirating")
	fi.write("\n"+i+"\n    "+l.get_text()+"\n")
fi.close()
f.close()
print("Your output has been saved in newbooks.txt located in the Desktop")