# habra_proxy - simple quasi proxy server based on uWSGI

**habra_proxy** - mirrors site,  plus provides content filtering options

## Run habra_proxy
```
uwsgi --ini habra_uwsgi.ini
```
## Initialization
There are 2 initialization files:
1) habra_uwsgi.ini - to initialize uWSGI and set **habra_proxy** http port
```
[uwsgi]
module = habra_proxy 
http = :8000
```
2) habra_init.py - to set url of the site to mirror for **habra_proxy**, and http port
```
HABRA_URL = "https://habrahabr.ru"
HTTP_PORT = ":8000"
PROXY_URL = "http://127.0.0.1" + HTTP_PORT
```
## Requirements
```
uWSGI==2.0.15
bs4==0.0.1
html5lib==0.999999999
requests==2.18.4
```
