# habra_proxy - simple quasi proxy server based on uWSGI (Python 2.7 version)

**habra_proxy** - mirrors site,  plus provides content filtering options

## Run habra_proxy
```
uwsgi --ini habra_uwsgi.ini
```
## Initialization
There are 2 initialization files (**habra_uwsgi.ini**, **habra_init.py**):

1) **habra_uwsgi.ini** - to initialize uWSGI and set **habra_proxy** http port
```
[uwsgi]
module = habra_proxy 
http = :8000
```
2) **habra_init.py** - to set url of the site to mirror for **habra_proxy**, and http port
```
HABRA_URL = "https://habrahabr.ru"
HTTP_PORT = ":8000"
PROXY_URL = "http://127.0.0.1" + HTTP_PORT

WORD_LENGTH = 6
TRADEMARK = u'™'
PATTERN = ur'\b(?P<xword>\w{%d})\b' % WORD_LENGTH
```
## Requirements
```
uWSGI==2.0.15  # Python 2.7 version
bs4==0.0.1
html5lib==0.999999999
requests==2.18.4
```
