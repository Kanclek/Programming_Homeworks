import requests
from bs4 import BeautifulSoup

def parse_page (url, separaters_lists=None):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        result = {}

        title = soup.title.string if soup.title else "Заголовок не найден"
        result["title"] = title

        if separaters_lists is not None:
            for selector in separaters_lists:
                elements = soup.select(selector)
                result[selector] = [elem.get_text(strip=True) for elem in elements]

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
     
    with open("output.txt", "w", encoding="utf-8") as f:
        for key, value in result.items():
            if isinstance(value, list):
                f.write(f"{key}\n")
                for item in value:
                    f.write(f" - {item}\n")
            else:
                f.write(f"{key}: {value}\n")

print("Данные сохранены в output.txt")

if __name__== "__main__":
  url = input("Введите URL для парсинга:")
  separaters_list = input("Разделители для парсинга":)
  if separaters_list:
      separaters_list = separaters_list.split()

  parse_page(url, separaters_list)
  
  