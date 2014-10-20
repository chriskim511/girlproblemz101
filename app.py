from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/<post>")
def post(post):
    return render_template("postbase.html")
