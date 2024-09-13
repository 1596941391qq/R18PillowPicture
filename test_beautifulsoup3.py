import requests
from bs4 import BeautifulSoup
import re


def contains_three_digits(s):
    return bool(re.search(r'\d{3,}', s))


def contains_at_least_one_letter(s):
    return bool(re.match(r'^(0|[A-Z])', s))


def find_a(url, func):
    """寻找a标签并返回字典 地址，判断方法"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    a_tags = soup.find_all("a")
    link_dict = {}
    for a_tag in a_tags:
        if func(a_tag.text):
            link_text = a_tag.text.strip()
            link_href = a_tag.get("href")
            link_dict[link_text] = link_href
    return link_dict


url = "http://166.88.55.27/"
link_list = list(find_a(url,contains_three_digits).values())
genshin_link = link_list[2]
url2 = url+genshin_link
genshin_dict = find_a(url2,contains_at_least_one_letter)
genshin_dict = {k: v for k, v in genshin_dict.items() if k[0].isupper() and '图片' not in k and '-' not in k and 'RSS' not in k and 'Piwigo' not in k}
genshin_dict={k[1:]: v for k, v in genshin_dict.items() if len(k) > 1}
genshin_dict = {k: url + v for k, v in genshin_dict.items()}

