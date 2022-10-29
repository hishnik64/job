from sqlalchemy.orm import sessionmaker

from DataSettings.create_table import DeclarBase
from DataSettings.send_in_base import TestSend
from static.app import engine



def main():
    TestSend()


    if __name__ == "__main__":
        return main()
