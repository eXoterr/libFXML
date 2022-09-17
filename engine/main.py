from .parsers.json import JSONParser
from .page import FXMLPage

import requests

# if __name__ == "__main__":
#     parser = JSONParser({})
#     resp = requests.get("http://spiderxml.com")
#     page = parser.parse_page(resp)
#     for i in page.items:
#         print(i)

def open_url(url: str) -> FXMLPage:
    parser = JSONParser({})
    resp = requests.get(url)
    page = parser.parse_page(resp)
    return page