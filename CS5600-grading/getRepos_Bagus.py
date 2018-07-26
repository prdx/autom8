import urllib.request
import base64
import json
import os
import shutil

ORGS = 'Summer18CS5600'
API_TOKEN = ''
GIT_API_URL = 'https://api.github.com'

MYUSERNAME = input("What is your github Username: ")
os.system("stty -echo")
MYPASSWORD = input("What is your password: ")
os.system("stty echo")
print("\n")

def get_repos(url):
    result = None
    request = urllib.request.Request(GIT_API_URL + url + '?per_page=200')
    base64string = base64.encodestring(('%s/token:%s' % (MYUSERNAME, API_TOKEN)).encode()).decode().replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib.request.urlopen(request)
    data = result.read()
    encoding = result.info().get_content_charset('utf-8')
    res = json.loads(data.decode(encoding))
    result.close()
    return res

cloneURL = []
res = get_repos('/orgs/' + ORGS + '/repos')

for r in res:
    os.system('git clone https://' + MYUSERNAME + ':' + MYPASSWORD + '@github.com/' + ORGS + '/' + r['name'])

# Count repo
print('Count repos: ', len(res))


