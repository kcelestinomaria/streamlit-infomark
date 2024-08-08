import streamlit as st 
from openbb import obb 
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

personal_access_token = os.getenv('PAT')

st.title('My Streamlit App')
st.write('Hello, Streamlit!')

obb.account.login(pat=personal_access_token)