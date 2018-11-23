import requests


def get(url, params={}, cookies={}, headers={}):
    res = requests.get(url, params=params, headers=headers, cookies=cookies)
    print(res.status_code)
    
    try:
        res.raise_for_status()
        return res
    except requests.exceptions.HTTPError:
        return None


def post(url, params={}, cookies={}, headers={}):
    res = requests.post(url, data=params, headers=headers, cookies=cookies)
    print(res.status_code)
    
    try:
        res.raise_for_status()
        return res
    except requests.exceptions.HTTPError:
        return None