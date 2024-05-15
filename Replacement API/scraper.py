import re
import requests
from bs4 import BeautifulSoup

URL = "https://hpk.edu.ua/replacements"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0",
    "referer": "https://hpk.edu.ua/"}


def get(tag):
    req = requests.get(URL, headers=HEADERS)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    lst = soup.find(class_="news-body").find_all(tag)
    lst = [item.text.strip().split("\n") for item in lst]

    return lst


def get_date_replacement():
    text = ' '.join(list(map(str, get("strong"))))
    date_pattern = r'\d{1,2}\s\w+\s\d{4}'
    matches = re.findall(date_pattern, text)
    return matches[0].split()


def get_replacement():
    lst = get("tr")
    for i in lst:
        if len(i) == 4 and i[1] == '\xa0':
            i.insert(0, '\xa0')
            i.insert(2, '\xa0')
        else:
            if not validate_format(i[0]):
                while len(i) != 6:
                    i.insert(0, '\xa0')

    for i in lst:
        if len(i) != 6:
            while len(i) != 6:
                i.append('\xa0')
    return lst


def validate_format(input_string):
    lst = input_string.split("-")
    if len(lst[0]) == 2 and len(lst[1]) == 3:
        return True
    else:
        return False
