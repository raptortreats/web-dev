from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as url

apple = url('https://www.flipkart.com/search?q=apple+mobiles&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=apple+mobiles&requestId=5e21fc5c-dff2-4485-8f4c-657dcba0ce2c&as-searchtext=apple')


# opening the conection
mobile_html = apple.read()
apple.close()

mobile_soup = soup(mobile_html, "html.parser")
# print(mobile_soup.head)
# print(mobile_soup.p)

# grabs the product
iphones = mobile_soup.findAll("div", {"class": "_3wU53n"})
print(len(iphones))  # total items

firstproduct = iphones[0]
tenthprdct = iphones[10]
print(firstproduct)
print(tenthprdct)

# no of ratings of mobiles
mob_rating = mobile_soup.findAll("span", {"class": "_38sUEc"})
print(len(mob_rating))
print(mob_rating[10].text)


# specs of mobiles
mob_specs = mobile_soup.findAll("ul", {"class": "vFw0gD"})
print(len(mob_specs))
print(mob_specs[10].text)


# star rating of mobiles
star_rating = mobile_soup(
    "div", {"class": "hGSR34"})
print(len(star_rating))
print(star_rating[10].text)


# details about 15th mobile
print(iphones[14].text)
print(mob_rating[14].text)
print(star_rating[14].text)
print(mob_specs[14].text)
