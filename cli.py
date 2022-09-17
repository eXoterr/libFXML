from engine.main import open_url

if __name__ == "__main__":
    base_url = input("Enter fxml url: ")
    while True:
        page = open_url(base_url)
        
        print("Urls:")

        for i in range(len(page.items) - 1):
            print(f'{i} {page.items[i]}')

        selected = int(input("Select url: "))
        base_url = page.items[selected].url