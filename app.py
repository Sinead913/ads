from flask import Flask, json, Response

app = Flask(__name__)

adverts = [
    {
        "advertid": 1,
        "keyword": 'network',
        "advert": "Network Engineer Job available in Belfast!"
    },
    {
        "advertid": 2,
        "keyword": 'network',
        "advert": "These are the best networks in the world!"
    },
    {
        "advertid": 3,
        "keyword": 'test',
        "advert": "Testing role available in Belfast IT company!"
    }
]

@app.route('/')
def get_all_ads():
    ads = []
    for advert in adverts:
        ads.append(advert["advert"])
    j = json.dumps(ads)
    rep = Response(j)
    rep.headers['Content-Type'] = "application/json"
    rep.headers['Access-Control-Allow-Origin'] = '*'
    return rep

@app.route('/adverts/<string:key>', methods=['GET'])
def get_ads(key):
    ads=[]
    for advert in adverts:
        if(key == advert["keyword"]):
            ads.append(advert["advert"])
    j = json.dumps(ads)
    rep = Response(j)
    rep.headers['Content-Type'] = "application/json"
    rep.headers['Access-Control-Allow-Origin'] = '*'
    return rep

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
