from sqlalchemy import create_engine

db_name = 'owlappdb'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'

# Connect to the database
#db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db_string = "postgresql://owlappdb:secret@localhost:5432/owlappdb"
db = create_engine(db_string)

def insert_comment(targetId, textFr, textEn, publishedAt, authorId):
    # Insert a new comment in the db
    query = """INSERT INTO owlappdb VALUES (
    %s,%s,%s,%s,%s,%s)"""
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

def test():
    liste = get_comments('Photo-51515')
    for i in liste:
        print (i)


if __name__ == '__main__':
    test()
