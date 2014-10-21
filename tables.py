import sqlite3

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
    q = "SELECT title,post,comments FROM posts,comments WHERE posts.id = comments.id and title = " + title
    result = c.execute(q)
    return result #Returns the title, the post, all the comments

#Inserts a new title and post into the database
def insert(title, post):
    q = "INSERT INTO posts VALUES('%s','%s',ROWID)" % (title,post)
    c.execute(q)

#Inserts a comment for a certain title into the database
def comment(title, comment):
    q = "SELECT id FROM posts WHERE title = " + title
    result = c.execute(q)
    q = "INSERT INTO comments VALUES('%s','%s')" % (comment,result) 
    
