import requests
import json



def get_news():
    url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=3fc0e943d72149ed83a74d7d556c3082'
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=3fc0e943d72149ed83a74d7d556c3082'
