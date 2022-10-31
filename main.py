from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Identity
from sqlalchemy.types import Enum




class Choices(Enum):
    user = 'user'
    admin = 'admin'


engine = create_engine("postgresql+psycopg2://postgres:161322@localhost/Employees", echo=True)
meta = MetaData()

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True, auto_increment=True),
    Column('name', String, nullable=False),
    Column('surname', String, nullable=False),
    Column('password', String, nullable=False),
    Column('phone_number', String, nullable=False),
    Column('job_title', String, nullable=False),
    # Column('role', choices=(('admin', 'Администратор'), ('user', 'Пользователь')), default='user'),
    # ChoiceType({"short": "short", "medium": "medium", "tall": "tall"})
    #Column('role', String, Enum(Choices)),
)
meta.create_all(engine)


statement = users.insert().values(name='долбаёб',
                                   surname='хуев',
                                   password='161322',
                                   phone_number='gji`k yf[eq',
                                   job_title ='Пидарас по жизни'
                                   )
engine.execute(statement)
ins= users.insert()
print(str(ins))
