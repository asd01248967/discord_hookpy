import requests, json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def api():
    r = request.json
    for alerts in r['alerts']:
        #這邊加一個for迴圈dict.key()alerts可以輪巡出alerts有多少告警，之後再試試看!
        if alerts['status'] == "resolved":
            color = 182388
        else:
            color = 16711680
    payload = {
        "username": r['receiver'],
        "embeds": [{
            "title": (r['status']).upper() + ' ：' + '[ ' + alerts['labels']['alertname'] + ' ]',
            "description": alerts['annotations']['description'],
            "color": color,
            "fields": [
                {
                    "name": "severity",
                    "value": alerts['labels']['severity'],
                    "inline": "true"
                },
                {
                    "name": "hostname",
                    "value": alerts['labels']['instance'],
                    "inline": "true"
                },
                {
                    "name": "summary",
                    "value": alerts['annotations']['summary'],
                    "inline": "false"
                }
            ]
        }]
    }
    response = requests.post('https://discordapp.com/api/webhooks/679215590258507778/iC4SXpabRqB5PrGNfx7HpFXbZccaU1K-BE6oIpqTW8GUOQ17LuQk3UQXBRryL1SotyRy', json=payload, headers = {"Content-Type": "application/json"})
    print(response.status_code)
    return 'hello'

app.run(host='0.0.0.0')