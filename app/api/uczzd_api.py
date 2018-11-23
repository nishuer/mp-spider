from . import request
from app.source import uczzd_source


def joke():
    res = request.get(uczzd_source.joke)

    if (res):
        list = []
        articles = res.json()['data']['articles']
        
        for item in articles:
            list.append(articles[item]['url'])

        return tuple(list)

    return ()