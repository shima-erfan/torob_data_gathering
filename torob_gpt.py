import requests
from bs4 import BeautifulSoup
import pandas as pd

url      = 'https://torob.com/browse/435/%D8%AA%D8%AC%D9%87%DB%8C%D8%B2%D8%A7%D8%AA-%D8%AD%D9%85%D9%84-%DA%A9%D9%88%D8%AF%DA%A9/'
titles = []
prices = []

for page_num in range(1, 3):
    page_url = f'{url}?page={page_num}'  # در صورت نیاز به پارامتر page در URL
    page     = requests.get(page_url)
    soup     = BeautifulSoup(page.text, 'html.parser')

    # تغییر انتخاب‌کننده‌ها به کلاس‌هایی که ثابت هستند
    title_elements = soup.select('h2')  # انتخاب دقیق‌تر با کلاس مناسب
    for t in title_elements:
        name = t.text.strip()
        titles.append(name)

    price_elements = soup.select('div.product-price-text')
    for p in price_elements:
        pr = p.text.strip()
        prices.append(pr)

# بررسی اینکه طول لیست‌ها برابر است
if len(titles) == len(prices):
    products = {'Title': titles, 'Price': prices}
    data     = pd.DataFrame(products)
    data.to_excel('product.xlsx', index=False)
    print("Data saved to product.xlsx")
    print(len(titles), len(prices))
else:
    print("Mismatch in the number of titles and prices!")   
