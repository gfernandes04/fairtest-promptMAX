def login(username, password, db):
    user = db.get_user(username)
    if user and user.password == password:
        return True
    return False

