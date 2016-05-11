from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route("/api/getTrace")
def getTrace():
    trace = {
        "trace_uuid": "asdasda",
        "transaction_uuid": "asdasdas",
        "origin_uuid": "adasdasd",
        "trace_name": "My Trace",
        "start_time": datetime(2016, 5, 11, 14, 14, 31, 100000).timestamp(),
        "end_time": datetime(2016, 5, 11, 14, 14, 33, 100000).timestamp(),
        "meta": {"some": "meta stuff"},
        "spans": [
            {
                "trace_uuid": "asdasda",
                "span_name": "service1",
                "start_time": datetime(2016, 5, 11, 14, 14, 31, 100000).timestamp()*1000,
                "end_time": datetime(2016, 5, 11, 14, 14, 31, 350000).timestamp()*1000,
                "meta": {"some": "meta stuff"}
            },
            {
                "trace_uuid": "asdasda",
                "span_name": "service2",
                "start_time": datetime(2016, 5, 11, 14, 14, 31, 200000).timestamp()*1000,
                "end_time": datetime(2016, 5, 11, 14, 14, 32, 350000).timestamp()*1000,
                "meta": {"some": "meta stuff"}
            },
            {
                "trace_uuid": "asdasda",
                "span_name": "service1",
                "start_time": datetime(2016, 5, 11, 14, 14, 31, 450000).timestamp()*1000,
                "end_time": datetime(2016, 5, 11, 14, 14, 32, 950000).timestamp()*1000,
                "meta": {"some": "meta stuff"}
            },
            {
                "trace_uuid": "asdasda",
                "span_name": "service3",
                "start_time": datetime(2016, 5, 11, 14, 14, 32, 100000).timestamp()*1000,
                "end_time": datetime(2016, 5, 11, 14, 14, 33, 100000).timestamp()*1000,
                "meta": {"some": "meta stuff"}
            },
        ]
    }
    return jsonify(**trace)


if __name__ == "__main__":
    app.run(debug=True)