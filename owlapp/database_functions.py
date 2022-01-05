from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to the database
db_string = os.getenv('DB_STRING')
db = create_engine(db_string)


def insert_comment(targetId, textFr, textEn, publishedAt, authorId):
    # Insert a new comment in the db, with auto-increment id
    query = """INSERT INTO owlappdb VALUES (DEFAULT,
    %s,%s,%s,%s,%s)"""
    values = [targetId, textFr, textEn, publishedAt, authorId]
    db.execute(query, values)


def get_comments(targetId):
    # Retrieve all comments matching a target ID
    query = """SELECT * FROM owlappdb WHERE targetId = %s;"""

    results = db.execute(query, targetId)

    res_list = []
    for row in results:
        res_list.append(row)

    return res_list


if __name__ == '__main__':
    print(db_string)
    print(type(db_string))
