from .parsers.json import JSONParser
from .page import FXMLPage

import requests

def open_fxml_url(url: str) -> FXMLPage:
    parser = JSONParser({})
    resp = requests.get(url)
    page = parser.parse_page(resp)
    return page