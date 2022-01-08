import requests
import json

def main(index=None):
    url = 'https://dbdrive.herokuapp.com/xls'
    myobj = {
        "index": index, 
        "identifier": "id",
        "xls": "https://docs.google.com/spreadsheets/d/1DM_-HOWXMsPmshnIq-wfJq7Jtc4pacLC6bUC8c1XzpU/edit?usp=sharing" 
    }

    req = requests.post(url, data = myobj)

    if req.status_code == 200:
        res = json.loads(req.content)
        return res['response']
    return None