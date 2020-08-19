import requests
from bs4 import BeautifulSoup
import csv



url = 'https://itti.com.np/gaming-laptops-nepal'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

containers = soup.findAll("div", {"class": "product details product-item-details box-info"})

with open('products.csv','w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['product_name', 'price'])

    for container in containers:
        model = container.h2.a.text.strip()
        prices = soup.findAll("div", {"class": "price-box price-final_price"})
        price = prices[0].span.span.text.strip()

        print('model' + model)
        print('price' + price)

        thewriter.writerow([model,price])
