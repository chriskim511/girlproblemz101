from flask import Flask, render_template, request, redirect, session
import collections
app=Flask(__name__)

dict=collections.OrderedDict()
dict["Introducing Pure"]="Blablabla"
dict["Everything You Need to Know About Grunt"]="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
fakecomments=["yes","no","maybe","so"]


@app.route("/",methods=["GET","POST"])
def home():
    title=request.form.get("title")
    material=request.form.get("material")
    #print title
    #print material
    #Add sqlite3 interface for title and material of posts
    return render_template("home.html",dict=dict)


@app.route("/<address>",methods=["GET","POST"])
def post(address):
    comment=request.form.get("comment")
    #print comment
    #Add sqlite3 interface to comments
    if(address in dict.keys()):
        return render_template("postbase.html",title=address,post=dict[address],comments=fakecomments )
    else:
        return render_template("null.html")

if __name__=="__main__":
    app.debug=True
    app.run()
