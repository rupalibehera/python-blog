import os
import datetime
import web


def get_db():
    conn = web.database(dbn='mysql', host=os.getenv('MYSQLDB_SERVICE_HOST',"localhost"), port=3306,db='blog', user=os.getenv('MYSQL_USER', "root"), pw=os.getenv('MYSQL_PASSWORD', "root"))
    conn.query("CREATE TABLE IF NOT EXISTS entries (id INT AUTO_INCREMENT, title TEXT, content TEXT, posted_on DATETIME, primary key (id));")
    return conn

def get_posts():
    return get_db().select('entries', order='id DESC')

def get_post(id):
    try:
        return get_db().select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(title, text):
    get_db().insert('entries', title=title, content=text, posted_on=datetime.datetime.utcnow())

def del_post(id):
    get_db().delete('entries', where="id=$id", vars=locals())

def update_post(id, title, text):
    get_db().update('entries', where="id=$id", vars=locals(),
        title=title, content=text)