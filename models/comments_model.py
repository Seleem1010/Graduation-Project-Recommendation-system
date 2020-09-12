from .db import DB
db = DB().db


def add_comment(text, time, pid, uid):
    id = DB.generate_random_id()
    c = db.cursor()
    c.execute(
        f'INSERT INTO comments (id, text, time, pid, uid) values ({id}, "{text}", "{time}", {pid}, {uid})')
    res = c.rowcount
    db.commit()
    c.close()
    return res


def edit_comment(id, text):
    c = db.cursor()
    c.execute(f'UPDATE comments SET text = "{text}" WHERE id = {id}')
    res = c.rowcount
    db.commit()
    c.close()
    return res


def delete_comment(id):
    c = db.cursor()
    c.execute(f'DELETE FROM comments where id = {id}')
    res = c.rowcount
    db.commit()
    c.close()
    return res
