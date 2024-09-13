import requests
from bs4 import BeautifulSoup



url = "https://pbase.com/hougong/newgallery335&view=tree"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
a_tags = soup.find_all("a")
link_dict = {}
name_tag="（继续点进去）"
for a_tag in a_tags:
    if name_tag in a_tag.text:
        link_text = a_tag.text.strip(name_tag)
        link_href = a_tag.get("href")
        link_dict[link_text] = link_href










