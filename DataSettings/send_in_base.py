from sqlalchemy.orm import sessionmaker

from DataSettings.create_table import Users, DeclarBase
from static.app import engine

class TestSend():
    new_post = Users(name='Серёга',
                     surname='Ковалик',
                     phone_namber='+79823058256',
                     user_name='user1',
                     password='1111',
                     job_title='кладовщик',
                     role='user'
                     )

    DeclarBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(new_post)
    session.commit()

    for post in session.query(Users):
        print(post)



