import requests
from lxml import html

def get_stock_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Проверяем на ошибки HTTP
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    
    tree = html.fromstring(response.content)
    
    # Альтернативные XPATH на случай изменения структуры страницы
    price_xpaths = [
        r'//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span/text()'
    ]


    price = None
    for xpath in price_xpaths:
        elements = tree.xpath(xpath)
        if elements:
            price = elements[0]
            break
    
    if price:
        return price.strip()
    else:
        print("Price not found. Page structure might be changed.")
        return None

if __name__ == "__main__":
    ticker = "AAPL"
    price = get_stock_price(ticker)
    
    if price is not None:
        print(f"Current price of {ticker}: {price}")
    else:
        print("Failed to retrieve price.")



#https://finance.yahoo.com/quote/AAPL
