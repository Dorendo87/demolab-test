#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, jsonify
import os
import subprocess
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/check-platform')
def check_platform():
    """
    Checking platform
    """
    output = subprocess.run(["uname", "-r"], stdout=subprocess.PIPE)
    sout = str(output)

    if "ph3-esx" in sout:
        data = "VMware Tanzu Platform"
        return jsonify(data)
    elif "4.18.0-305.el8.x86_64" in sout:
        data = "Red Hat VM"
        return jsonify(data)
    elif "5.4.14" in sout:
        data = "Google Kubernetes Engine"
        return jsonify(data)
    else:
        data = "Red Hat OpenShift Container Platform"
        return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
