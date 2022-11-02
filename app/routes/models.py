from sqlalchemy import Column, Integer, String
from app.database.models import db

import alembic
class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
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

    def __init__(self, name, surname, password, phone_number, job_title):
        self.name = name
        self.surname = surname
        self.password = password
        self.phone_number = phone_number
        self.job_title = job_title

    @property
    def full_info(self):
        return f'{self.id} {self.name} {self.surname} {self.job_title} {self.phone_number} {self.password}'

    def __repr__(self):
        info: str = f'Имя:{self.name} Фамилия:{self.surname}, ' \
                    f'Телефон: {self.phone_number}, Должность:{self.job_title}'
        return info
