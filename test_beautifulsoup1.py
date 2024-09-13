import requests

from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from test_beautifulsoup2 import link_dict
from test_beautifulsoup3 import genshin_dict

website_url=[]
print(link_dict)
print(genshin_dict)

def find_photo(name_to_find):
    url = link_dict.get(name_to_find, None)
    url2 = genshin_dict.get(name_to_find, None)
    if url is None and url2 is None:
        print(f"{name_to_find} 不在字典中。")
        return None
    website_url.append(url)
    website_url.append(url2)
    img_urls = []

    def extract_images(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        img_tags = soup.find_all("img")
        for img_tag in img_tags:
            img_url = img_tag.get("src")
            if img_url.endswith(".jpg") or img_url.endswith(".JPEG"):
                img_urls.append(img_url)

    if url is not None:
        extract_images(url)
    # 检查url2
    if url2 is not None:
        extract_images(url2)

    return img_urls


def view_preview_image(image_urls):
    if image_urls is None:
        return
    for image_url in image_urls:
        try:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            image.show()
        except requests.exceptions.RequestException as e:
            image_url='http://166.88.55.27/'+image_url
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            image.show()
        except IOError as e:
            print(f"Error opening image: {e}")



