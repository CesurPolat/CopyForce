from codecs import utf_8_encode
import json
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/api/Test")
def hello():
    f=open("games.json","r")
    output=[]
    for x in f.readlines():
        output.append(x.encode().decode('utf-8'))
    return {"data":output}

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    print("Api is running")