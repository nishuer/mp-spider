from . import request
import datetime


base_url = 'https://mlab.toutiao.com/api/issues/rise'
base_params = {
    "rid": 0,
    "xschema": "https"
}
cids = {
    "star": 1629,
    "history": 1655,
    "pet": 46073964
}


def getRiseDate():
    today = datetime.date.today()
    return today + datetime.timedelta(days=-3)


def getRiseKeyword(type):
    base_params['cid'] = cids[type]
    base_params['start'] = getRiseDate()
    base_params['end'] = getRiseDate()

    res = request.get(base_url, base_params)

    if (res):
        list = []
        issues_rise = res.json()['issues_rise']
        
        for item in issues_rise:
            list = list + item['keywords']

        return tuple(set(list))

    return ()