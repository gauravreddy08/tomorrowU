import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from datetime import datetime

# tab1, tab2 = st.tabs(["Questions", "Answers"])

# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

service_account= {
  "type" : st.secrets['firebase']['type'],
  "project_id" : st.secrets['firebase']['project_id'],
  "private_key_id" : st.secrets['firebase']['private_key_id'],
  "private_key" : st.secrets['firebase']['private_key'],
  "client_email" : st.secrets['firebase']['client_email'],
  "client_id" : st.secrets['firebase']['client_id'],
  "auth_uri" : st.secrets['firebase']['auth_uri'],
  "token_uri" : st.secrets['firebase']['token_uri'],
  "auth_provider_x509_cert_url" : st.secrets['firebase']['auth_provider_x509_cert_url'],
  "client_x509_cert_url" : st.secrets['firebase']['client_x509_cert_url'],
  "universe_domain" : st.secrets['firebase']['universe_domain']
}

if not firebase_admin._apps:
    database_url = st.secrets['DB_URL']

    cred = credentials.Certificate(service_account)
    firebase_admin.initialize_app(cred, {
        'databaseURL': database_url
    })

database = db.reference('/')
st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("#")


answer = st.text_input("What would tommorow you want you today to do?")

if answer:
    database.push({"answer": answer,
                    "date": datetime.now().strftime("%d%m%y:%H%M%S")})
