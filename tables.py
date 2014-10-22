import sqlite3
import os

def create():
    if not os.path.isfile("posts.db"):
        conn = sqlite3.connect("posts.db")
        c = conn.cursor()
        #Create the two tables with titles, posts, and comments
        q = "create table posts (title text unique, post text, id integer)"
        c.execute(q)
        q = "create table comments (comments text, id integer)"
        c.execute(q)
        conn.commit()

#Gets the post and comments for a title
def get(title):
    conn = sqlite3.connect("posts.db")
    c = conn.cursor()
    q = "SELECT title,post,comments FROM posts,comments WHERE posts.id = comments.id and title = " + title
    result = c.execute(q)
    conn.commit()
    return result #Returns the title, the post, all the comments

def getComments(title):
    conn = sqlite3.connect("posts.db")
    c = conn.cursor()
    q = "SELECT comments FROM posts,comments WHERE posts.id = comments.id and title = " + title
    result = c.execute(q)
    conn.commit()
    return result #Returns all the comments

#Inserts a new title and post into the database
def insert(title, post):
    conn = sqlite3.connect("posts.db")
    c = conn.cursor()
    q = "INSERT INTO posts VALUES('%s','%s',1)" % (title,post)
    c.execute(q)
    conn.commit()
    
#Inserts a comment for a certain title into the database
def comment(title, comment):
    conn = sqlite3.connect("posts.db")
    c = conn.cursor()
    q = "SELECT id FROM posts WHERE title = " + title
    result = c.execute(q)
    q = "INSERT INTO comments VALUES('%s','%s')" % (comment,result)
    c.execute(q) 
    conn.commit() 
