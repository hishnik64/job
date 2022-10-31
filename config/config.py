from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:161322@localhost/Employees", connect_args={"check_same_thread":False})