# mp_spider

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

## Run Development

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run --host=0.0.0.0
```

## Run Production

```bash
gunicorn -w 4 -b 127.0.0.1:8000 manage:app -D
```

## devOps Cli

```bash
ps ax|grep gunicorn
pstree -ap|grep supervisor

nginx -s reload

sudo systemctl enable mysqld
sudo systemctl start mysqld
sudo systemctl status mysqld
```
