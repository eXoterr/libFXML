from .utils import clear_styles

class FXMLItem:
    def __init__(self, title: str, logo: str, kind: int, description="", submenu=None, url="") -> None:
        self.title = clear_styles(title)
        self.logo = logo
        self.kind = kind
        self.description = clear_styles(description)
        self.submenu = submenu
        self.url = url

    def __str__(self) -> str:
        return str([self.title, self.kind, self.url])

        

class FXMLPage:
    def __init__(self, icon: str, title: str, url: str, items=[]) -> None:
        self.__icon = icon
        self.__title = clear_styles(title)
        self.__url = url
        self.__items = items

    @property
    def icon(self):
        return self.__icon

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def items(self):
        return self.__items

    def __str__(self) -> str:
        return str([self.__url, self.__title, self.__items])



