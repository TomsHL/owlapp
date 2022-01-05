from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = str(os.getenv("DB_PORT"))

# Connect to the database
#db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
# Uncomment next line and comment previous one for local testing on UNIX
db_string = "postgresql://owlappdb:secret@localhost:5432/owlappdb"
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
    pass
