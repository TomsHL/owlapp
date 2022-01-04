CREATE TABLE IF NOT EXISTS owlappdb
(	id	TEXT,
    targetId TEXT,
    textFr TEXT,
    textEn TEXT,
    publishedAt TEXT,
  	authorId TEXT
);

INSERT INTO owlappdb VALUES ( 'id0001', 'Comment_5547', 'Bonne idée', 'Good idea', '54165445674', 'Tom55');
INSERT INTO owlappdb VALUES ( 'id0002', 'Comment_5547', 'Mauvaise idée', 'Bad idea', '48544844', 'Georges88');
INSERT INTO owlappdb VALUES ( 'id0003', 'Photo-51515', 'Belle photo!', 'Nice picture!', '4515457457', 'Pierre998');
