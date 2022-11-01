from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Identity
from sqlalchemy.orm import sessionmaker, Query
from models.database import Session
from models.database import Base
from sqlalchemy.orm import query


class Users(Base):
    __tablename__ = 'users'
    ROLE = [
        ('user', 'Пользователь'),
        ('admin', 'Администратор')
    ]
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    job_title = Column(String, nullable=False)

    # role = Column(sqlalchemy.util.type.choice.ChoiceType(ROLE), default=u'user')


    @property
    def full_info(self):
        return f'{self.id} {self.name} {self.surname} {self.job_title} {self.phone_number} {self.password}'

    def __repr__(self):
        info: str = f'Имя:{self.name} Фамилия:{self.surname}, ' \
                    f'Телефон: {self.phone_number}, Должность:{self.job_title}'
        return info


users = [
    Users(name='бля', surname='Пидарасович', password='1231231', phone_number='13131313123',
          job_title='dsfsdfsdfsfsdfdsfsdf')
]

session_maker = sessionmaker(bind=create_engine("postgresql+psycopg2://postgres:161322@localhost/Employees"))


def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

def update_db():
    with session_maker() as session:
        id_user = session.query(Users).filter_by(name='бля').first()
        id_user.name = 'блядство'
        session.commit()



def del_user():
    with session_maker() as session:
        id_user = session.query(Users).filter_by(name='бля').first()
        session.delete(id_user)
        session.commit()

def show_db():
    with session_maker() as session:
        user_records = session.query(Users).all()
        for user in user_records:
            print(" " * 100)
            print(user)


update_db()
show_db()
