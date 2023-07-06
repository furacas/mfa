import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, String, Column
from sqlalchemy.orm import declarative_base

# Setup SQLite connection and ORM
engine = create_engine('sqlite:///mfa_data.db')
Base = declarative_base()

class MFA(Base):
    __tablename__ = 'mfa'
    account = Column(String, primary_key=True)
    secret = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

st.title('Add MFA Account')

account = st.text_input('Account Name')
secret = st.text_input('MFA Secret')

if st.button("Submit"):
    session = Session()
    session.add(MFA(account=account, secret=secret))
    session.commit()
    st.success("Saved MFA details!")
