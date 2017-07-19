import re
import requests

item_price = open('price.txt', 'a')
with open('url_file.txt') as f:
    url = f.read().strip().split(',')
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
          'Connection':'keep-alive',
                    }
i = 0
for i in range(52):
    if i < 52:
        page_url = requests.get(url[i], headers=header)
        page = page_url.text
        price = re.findall('<span id="priceblock_saleprice" class="a-size-medium a-color-price"(.*?)</span>', page, re.S)
        print(price, file=item_price)
    else:
        print('Finish')
        
html = urlopen('https://www.amazon.com/dp/B00CRR5L8U')
bsobj = BeautifulSoup(html, "html.parser")
price = bsobj.findAll('span', {'id': 'priceblock_saleprice'})
print(price[0].get_text())
