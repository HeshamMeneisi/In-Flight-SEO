# API client

import json
from urllib.request import urlopen


def get_article_details(slug):
    url = f"https://www.example.com/articles/{slug}"
    response = urlopen(url)
    return json.loads(response.read())
