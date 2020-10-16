from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.flipkart.com/search?q=pocof1&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", { "class": "col col-5-12 _2o7WAb"} )
#print(len(containers))

#print(soup.prettify(containers[0]))

container = containers[0]
# to print phone name
#print(container.div.img["alt"])


# Scraping Price
price = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
print(price[0].text)


# Scraping Rating
rating = container.findAll("div", {"class": "hGSR34"})
print(rating[0].text)

#container = containers[0]

#print(container.div.img(["alt"]))

#price = container.findAll("div", {"class" : "_3O0U0u"})

#print(price[0].text)

#filename = "name_price_rating.csv"



f = open(filename, "w")

headers = ("Product_name, Pricing, Ratings\n")
f.write(headers)


for container in containers:
    product_name = container.div.img["alt"]
    
    price_container = container.findAll("div", {"class": "_3O0U0u"})
    price = price_container[0].text.strip()
    
    raring_container  = container.findAll("div", {"class": "hGSR34"})
    rating = rating_container[0].text





