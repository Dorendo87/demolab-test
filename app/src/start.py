#!/usr/bin/env python

"""
Purpose: A simple Flask web app that demonstrates Entity WEALTH Tracker
"""

from flask import Flask, render_template, request, url_for, redirect, jsonify
from mysql_config import dbConfig
import mysql.connector as pyo
from flask_cors import CORS, cross_origin

con = pyo.connect(**dbConfig)

app = Flask(__name__)
CORS(app)

@app.route('/accountid')
def index():
    if request.method == "GET":
        acctid = request.args.get("query")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM exercisedb.clientdemo WHERE accountid=%s", (acctid,))
        data = cursor.fetchall()
        cursor.close()

        amount = data[0][2]
        if amount > 100000:
            data.append("gold")
        else:
            data.append("silver")
        return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
