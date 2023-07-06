import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, String, Column
from sqlalchemy.orm import declarative_base
import pyotp
import time

# Setup SQLite connection and ORM
engine = create_engine('sqlite:///mfa_data.db')
Base = declarative_base()

class MFA(Base):
    __tablename__ = 'mfa'
    account = Column(String, primary_key=True)
    secret = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

st.set_page_config(page_title="View MFA Codes")
st.title('View MFA Codes')


for row in session.query(MFA).all():
    st.subheader(f"Account: {row.account}")

    # Create OTP object
    totp = pyotp.TOTP(row.secret)

    # Display OTP and countdown
    remaining = totp.interval - time.time() % totp.interval
    st.write(f"OTP: {totp.now()}")
    st.write(f"Time remaining: {remaining:.2f}s")

    if st.button(f"Delete {row.account}"):
        session.delete(row)
        session.commit()
        st.success(f"Deleted {row.account}!")

time.sleep(1)
st.experimental_rerun()