from fastapi import FastAPI
from pytrends.request import TrendReq
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/trends")
def get_trends(keyword: str):
    try:
        pytrends = TrendReq(hl="en-US", tz=360)
        pytrends.build_payload([keyword], cat=0, timeframe="now 7-d", geo="US")
        data = pytrends.interest_over_time()
        if data.empty:
            return {"error": "No trend data available for this keyword"}
        return data[keyword].to_dict()
    except Exception as e:
        return {"error": str(e)}

@app.get("/recommendations")
def get_recommendations(keyword: str):
    try:
        # Новый URL с правильным запросом
        search_url = f"https://s.1688.com/selloffer/offer_search.htm?keywords={keyword}&spm=a260k.home2024.searchbox.0"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Отправка запроса
        response = requests.get(search_url, headers=headers)

        # Проверка, что запрос выполнен успешно
        if response.status_code != 200:
            return {"error": f"Failed to fetch data from 1688, status code: {response.status_code}"}

        # Печатаем содержимое страницы для отладки
        print(response.content[:500])  # Печатаем первые 500 символов HTML-страницы для анализа

        # Парсинг HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Пример парсинга — найдем все ссылки с товарами (поменял селектор на "offer-title")
        product_titles = [tag.text.strip() for tag in soup.find_all("a", class_="offer-title")]

        if not product_titles:
            return {"error": "No recommendations found"}
        
        return {"products": product_titles}
    
    except Exception as e:
    
        return {"error": str(e)}


def get_recommended_category_texnomart():
    try:
        # Новый URL с правильным запросом/category/ca
        search_url = f"https://gw.texnomart.uz/api/common/v1/search/filters?category_all=pylesosy&sort=-order_count&page=2"
        search_url = f"https://gw.texnomart.uz/api/web/v1/header/top-categories"
        
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        # }

        # Отправка запроса
        response = requests.get(search_url)

        # Проверка, что запрос выполнен успешно
        if response.status_code != 200:
            return {"error": f"Failed to fetch data from 1688, status code: {response.status_code}"}

        # Печатаем содержимое страницы для отладки
        print(response.content[:500])  # Печатаем первые 500 символов HTML-страницы для анализа

        # Парсинг HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Пример парсинга — найдем все ссылки с товарами (поменял селектор на "offer-title")
        product_titles = [tag.text.strip() for tag in soup.find_all("a", class_="offer-title")]

        if not product_titles:
            return {"error": "No recommendations found"}
        
        return {"products": product_titles}
    
    except Exception as e:
    
        return {"error": str(e)}

def get_popular_menu():
    try:
        # Новый URL с правильным запросом/category/ca
        search_url = f"https://gw.texnomart.uz/api/common/v1/search/filters?category_all=pylesosy&sort=-order_count&page=2"
        search_url = f"https://gw.texnomart.uz/api/web/v1/header/top-categories"
        
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        # }

        # Отправка запроса
        response = requests.get(search_url)

        # Проверка, что запрос выполнен успешно
        if response.status_code != 200:
            return {"error": f"Failed to fetch data from 1688, status code: {response.status_code}"}

        # Печатаем содержимое страницы для отладки
        print(response.content[:500])  # Печатаем первые 500 символов HTML-страницы для анализа

        # Парсинг HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Пример парсинга — найдем все ссылки с товарами (поменял селектор на "offer-title")
        product_titles = [tag.text.strip() for tag in soup.find_all("a", class_="offer-title")]

        if not product_titles:
            return {"error": "No recommendations found"}
        
        return {"products": product_titles}
    
    except Exception as e:
    
        return {"error": str(e)}

get_recommended_category_texnomart()
print('')
get_popular_menu()