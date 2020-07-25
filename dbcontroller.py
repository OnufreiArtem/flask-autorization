import sqlite3

def check_auth(username, password):
    db = sqlite3.connect('users.db')
    cmd = db.cursor()
    query = 'SELECT * FROM auth WHERE username="%s" AND password="%s";' % (username, password)
    print(query)
    cmd.execute(query)
    return len(cmd.fetchall()) >= 1
