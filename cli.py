#Example cli for libFXML
from engine.main import open_fxml_url

if __name__ == "__main__":
    url = input("Enter fxml url: ")
    while True:
        page = open_fxml_url(url)
        
        print("Urls:")

        for i in range(len(page.items) - 1):
            print(f'{i} {page.items[i]}')

        selected = int(input("Select url: "))
        url = page.items[selected].url