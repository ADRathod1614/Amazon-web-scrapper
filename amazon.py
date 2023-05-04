from bs4 import BeautifulSoup
import requests
import csv

url="https://www.amazon.in/gp/bestsellers/books"

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


page=requests.get(url,headers=headers)

soup=BeautifulSoup(page.content,"html.parser")

#get all books
books=soup.find_all(id="gridItemRoot")

CSV_headers=['Rank','title','Author','Price']

for book in books:
      
    rank=book.find('span',class_="zg-bdg-text").text[1:]

    children=book.find('div', class_='zg-grid-general-faceout').div

    title=children.contents[1].text
    author=children.contents[2].text
    price=children.contents[-1].text

    with open('amazon_book.csv','a',encoding='utf-8',newline='') as f:
       writer= csv.writer(f)
     
       writer.writerow([rank,title,author,price])
