import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 連接數據庫
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@fastDB:3306/fast"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# cnx = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# start db connection
# def get_db_session():
#     db = SessionLocal()
#     try:
#         yield db
#     except Exception:
#         db.rollback()
#         raise
#     finally:
#         db.close()
