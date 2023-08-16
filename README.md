# mp-spider
Toutiao auto Posting robot and media platform spiders 今日头条自动发文机器人，各大公众平台采集爬虫，部分公众平台规则需要自己适配。

## Install Python 3 on CentOS 7

```bash
https://linuxize.com/post/how-to-install-python-3-on-centos-7

scl enable rh-python36 bash
```

## Create virtual environment

```bash
mkdir myproject
cd myproject
mac: python3 -m venv venv
windows: venv\Scripts\activate.bat
```

## Activate virtual environment

```bash
. venv/bin/activate
```

## Logout virtual environment

```bash
deactivate
```

## Install the dependencies

```bash
pip install -r requirements.txt
```

## Generate requirements.txt

```bash
pip freeze > requirements.txt
```
