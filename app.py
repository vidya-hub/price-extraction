from bs4 import BeautifulSoup
import requests


inputproduct=input("Enter Product Name :")
res = requests.get(
    f'https://www.flipkart.com/search?q={inputproduct}')
soup = BeautifulSoup(res.content, 'html.parser')
body = soup.find("body")
container = ((body.find("div", {"id": "container"})).find("div").find("div", {
             "class": "_36fx1h _6t1WkM _3HqJxg"})).find("div", {"class": "_1YokD2 _2GoDe3"})
products = (container.find_all("div", {"class": "_1YokD2 _3Mn1Gg"})[
            1]).find_all("div", {"class": "_1AtVbE col-12-12"})
product = products[0].find("div").find("div").find("div").find("a")

for pro in products:
    try:
        product = pro.find("div").find("div").find("div").find("a")
        spec_details = ((product.find(
            "div", {"class": "_3pLy-c row"})).find("div", {"class", "col col-7-12"}))
        price_details = ((product.find(
            "div", {"class": "_3pLy-c row"})).find("div", {"class", "col col-5-12 nlI3QM"}))
        title = spec_details.find_all("div")[0].text
        spec = spec_details.find_all("div")
        rating = (spec_details.find(
            "div", {"class", "gUuXy-"})).find_all("span")
        ratingval = rating[0].find("div").text
        reviews = rating[1].find("span").text
        price = (price_details.find("div").find_all("div")[0].find("div").text)
        print({"price": price, "title": title,
               "reviews": reviews, "rating": ratingval})
    except:
        # print(pro.find("div"))
        pass

# .find("div",{"class":"_1AtVbE col-12-12"})
