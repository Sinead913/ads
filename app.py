from flask import Flask, request, json, Response
import sqlalchemy
import pymysql

app = Flask(__name__)

db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        username="root",
        password="password",
        database="Adverts",
        query={"unix_socket": "/cloudsql/{}".format("cloudcomputing3032:us-central1:ads-index")},
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,  # 30 seconds
    pool_recycle=1800,  # 30 minutes
)

@app.route('/')
def get_ads():
    
    output = {
    "error": False,
    "ads": ""
    }
    ads=[]
    
    try:
        searchText = request.args.get('search')
        with db.connect() as conn:
            stmt = sqlalchemy.text("SELECT advert FROM advert WHERE keyword=:search")
            results = conn.execute(
                stmt, search=searchText
            ).fetchall()
            for row in results:
                ads.append(row[0])
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
