from flask import Flask, jsonify

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
    return jsonify(adverts)

@app.route('/adverts/<string:key>', methods=['GET'])
def get_ads(key):
    for advert in adverts:
        if(key == advert["keyword"]):
            return advert, 200
    return "User not found", 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
