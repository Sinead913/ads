from flask import Flask, request, json, Response

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
def get_ads():
    
    output = {
    "error": False,
    "ads": ""
    }
    ads=[]
    
    try:
        searchText = request.args.get('search')
    
        for advert in adverts:
            if(searchText == advert["keyword"]):
                ads.append(advert["advert"])
    except Exception as err:
        newOutput = { "error": str(err), "ads": "" }
        output.update(newOutput)
    else:    
        newOutput = { "error": False, "ads": ads }
        output.update(newOutput)
    finally:
        j = json.dumps(output)
        rep = Response(j)
        rep.headers['Content-Type'] = "application/json"
        rep.headers['Access-Control-Allow-Origin'] = '*'
        return rep

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
