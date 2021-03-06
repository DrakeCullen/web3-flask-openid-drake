from flask_login import UserMixin

from db import get_db

class User(UserMixin):
    ROLES=['user','admin']
    DEFAULT_ROLE='user'
    def __init__(self, id_, name, email, profile_pic, role):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.role = role

    @staticmethod
    def get(user_id):
        db = get_db()
        cursor = db.cursor()
        user = cursor.execute(
            "SELECT * FROM usertable WHERE id = %s", (user_id,)
        )
        user=cursor.fetchone()
        cursor.close()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3], role=user[4]
        )
        return user

    @staticmethod
    def create(id_, name, email, profile_pic, role):
        db = get_db()
        cursor=db.cursor()
        cursor.execute(
            "INSERT INTO usertable (id, name, email, profile_pic, role) "
            "VALUES (%s, %s, %s, %s, %s)",
            (id_, name, email, profile_pic, role),
        )
        cursor.close()
        db.commit()