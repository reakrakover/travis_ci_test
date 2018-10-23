import requests
from bs4 import BeautifulSoup

url = "https://www.soccervista.com/bet.php"
home_selector = "#col1"
game_link_selector = "#col1 > div:nth-of-type(20) > table:nth-of-type(3) > tbody > tr.onem > td.detail > a"

r = requests.get(url, verify=False)
soup = BeautifulSoup(r.content, "html.parser")
link = soup.select("#search-results-list > li:nth-child(1) > div > div > div.col-xs-8.col-sm-9.card-meta-data > div.title-author-info > h3 > a")

draw_first_appear = str(soup).find("DRAW bet of the day")
slice_one = str(soup)[draw_first_appear:]

home_first_appear = slice_one.find('td class="home"')
slice_two = slice_one[home_first_appear:]

href_first_appear = slice_two.find("href=")
html_first_appear = slice_two.find(".html")
slice_three = slice_two[href_first_appear+6:html_first_appear+5]

final_url = "https://www.soccervista.com/{}".format(slice_three)

print(final_url)
