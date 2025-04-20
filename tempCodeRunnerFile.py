from flask import Flask,request 
from flask import render_template,url_for
from sender import hideFunc
from receiver import revealFunc
import os
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hide",methods=['POST','GET'])
def hide():
    if request.method == 'POST':
        formInfo=request.form
        result=hideFunc(formInfo['sec_msg'],formInfo['psw'],formInfo['cvr_msg'])
        return render_template("index.html",result=result)
    return render_template("index.html")

@app.route("/reveal",methods=['POST','GET'])
def reveal():
    if request.method == 'POST':
        formInfo=request.form
        result_reveal=revealFunc(formInfo['steg_msg'],formInfo['psw_rev'])
        return render_template("index.html",result_reveal=result_reveal)
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

