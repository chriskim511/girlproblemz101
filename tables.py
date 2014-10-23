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

def getPosts():
    conn = sqlite3.connect("posts.db")
    c = conn.cursor()
    q = "SELECT post FROM posts"
    result = c.execute(q)
    conn.commit()
    return result #Returns all the posts

def getTitles():
    conn = sqlite3.connect("posts.db")
    c = conn.cursor()
    q = "SELECT title FROM posts"
    result = c.execute(q)
    conn.commit()
    return result #Returns all the titles

#Obsolete function now
def loadDict():
    dict = {}
    titles = getTitles()
    posts = getPosts()
    for t,p in zip(titles,posts):
        dict[t[0]] = p[0] #Creates the dictionary to be used in HTML
    return dict

def getComments(title):
    conn = sqlite3.connect("posts.db")
    c = conn.cursor()
    q = "SELECT comments FROM posts,comments WHERE posts.id = comments.id and posts.title = '" + title + "'"
    result = c.execute(q)
    conn.commit()
    ret = []
    for r in result:
        ret.append(r[0])
    print ret
    return ret #Returns all the comments for a certain title

#Inserts a new title and post into the database
def insert(title, post):
    conn = sqlite3.connect("posts.db")
    c = conn.cursor()

    titles = getTitles()
    i = 0
    for x in titles:
        i = i + 1

    q = "INSERT INTO posts VALUES('%s','%s',%d)" % (title,post,i)
    c.execute(q)
    conn.commit()
    
#Inserts a comment for a certain title into the database
def comment(title, comment):
    conn = sqlite3.connect("posts.db")
    c = conn.cursor()
    q = "SELECT id FROM posts WHERE title = '" + title + "'"
    result = c.execute(q)
    q = "INSERT INTO comments VALUES('%s',%d)" % (comment,c.fetchone()[0])
    c.execute(q) 
    conn.commit() 
