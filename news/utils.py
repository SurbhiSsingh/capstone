# import requests

# def fetch_live_news():
#     url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_API_KEY"
#     response = requests.get(url)
#     data = response.json()

#     news = []
#     for item in data.get("articles", []):
#         news.append({
#             "title": item.get("title"),
#             "link": item.get("url"),
#             "published_date": item.get("publishedAt"),
#         })
#     return news
# utils.py
def fetch_live_news():
    print("📡 Fetching news...")  # Debug
    return [
        {'title': 'Test News 1', 'link': 'https://example.com/1', 'published_date': '2025-05-07'},
        {'title': 'Test News 2', 'link': 'https://example.com/2', 'published_date': '2025-05-07'}
    ]
