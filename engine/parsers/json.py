from engine.page import FXMLPage, FXMLItem
import json
import requests

class JSONParser:
    def __init__(self, config) -> None:
        self.config = config

    def parse_page(self, page: str | requests.Response) -> FXMLPage:
        
        raw_dict = dict()
        url = ""

        if isinstance(page, requests.Response):
            url = page.request.url
            page = page.text

        try:
            raw_dict = json.loads(page)
        except json.JSONDecodeError as e:
            raise e

        if "channels" in raw_dict and len(raw_dict['channels']) > 0:
            items = []
            for chan in raw_dict['channels']:
                items.append(self.__parse_item(chan))

        return FXMLPage(
            icon=raw_dict.get("icon"),
            title=raw_dict.get("title"),
            url=url,
            items=items
        )

    # kind 0 - Submenu (item in item)
    # kind 1 - Generic playlist (other page or website)
    # kind 2 - Generic streamable media (HLS, MP4, etc) 
    # kind 3 - Search input url 
    # kind 99 - Unknown/unimplemented item type
    @classmethod
    def __parse_item(cls, item: dict) -> FXMLItem:

        if "search_on" in item:
            kind = 3
            url = item.get("playlist_url")
        elif "playlist_url" and item['playlist_url'] == "submenu" in item:
            kind = 0
            url = item.get("playlist_url")
        elif "playlist_url" in item:
            kind = 1
            url = item.get("playlist_url")
        elif "stream_url" in item:
            kind = 2
            url = item.get("stream_url")
        else:
            kind = 99
            url = ""


        return FXMLItem(
            title=item.get("title"),
            logo=item.get("logo_30x30"),
            description=item.get("description"),
            kind=kind,
            url=url
        )
