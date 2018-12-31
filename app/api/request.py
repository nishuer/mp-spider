import requests


def get(url, params={}, cookies={}, headers={}, **kwargs):
    res = requests.get(url, params=params, headers=headers, cookies=cookies, **kwargs)
    print(res.status_code)
    
    try:
        res.raise_for_status()
        return res
    except requests.exceptions.HTTPError:
        return None


def post(url, params={}, cookies={}, headers={}, **kwargs):
    res = requests.post(url, data=params, headers=headers, cookies=cookies, **kwargs)
    print(res.status_code)
    
    try:
        res.raise_for_status()
        return res
    except requests.exceptions.HTTPError:
        return None