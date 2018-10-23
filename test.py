import requests
from bs4 import BeautifulSoup

url = "https://www.soccervista.com/bet.php"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# ---------------------------------------------------------
draw_first_appear = str(soup).find("DRAW bet of the day")
slice_one = str(soup)[draw_first_appear:]

home_first_appear = slice_one.find('td class="home"')
slice_two = slice_one[home_first_appear:]

href_first_appear = slice_two.find("href=")
html_first_appear = slice_two.find(".html")
slice_three = slice_two[href_first_appear+6:html_first_appear+5]

final_url = "https://www.soccervista.com/{}".format(slice_three)
print(final_url)
# ---------------------------------------------------------

r = requests.get(final_url)
soup = BeautifulSoup(r.content, "html.parser")
score = soup.find_all("td", {"class": "score"})

for i in score:
    print(i.text)
