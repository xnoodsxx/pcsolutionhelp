from wsgi import app, db, User

with app.app_context():
    sql_query = "INSERT INTO user (username, password, email, is_admin) VALUES ('AdminXds', 'scrypt:32768:8:1$29SdIBVx9hQqMbxP$3c8862d281ebbbaabcb1b9bdf2188b5ec8d506ec0040770ce85cf4193c00a93c9bdff4de958df6c1edd5552a900aa08e36d4ffccb2aaa3a8a2c9e657d5c7af9e', 'xno.oodsx@mail.ru', 1);"
    db.session.execute(db.text(sql_query))

    db.session.commit()

    users = User.query.all()
    for user in users:
        print(user.username, user.email, user.is_admin)
