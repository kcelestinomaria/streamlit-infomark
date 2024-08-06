"""News Page"""

from datetime import datetime, timedelta

from openbb import obb 
from openbb_biztoc.utils.helpers import get_all_tags, get_sources

import streamlit as st 

st.set_page_config(
    layout="wide",
    page_title="News",
    initial_sidebar_state="expanded",
)

st.sidebar.markdown(
    """
    <style>
    section[data-testid="stSidebar"] {
        top: 1% !important;
        height: 98.25% !important;
        left: 0.33% !important;
        margin-top: 0 !important;
    }
    section[data-testid="stSidebar"] img {
        margin-top: -75px !important;
        margin-left: -10px !important;
        width: 95% !important;
    }
    section[data-testid="stVerticalBlock"] {
        gap: 0rem;
    }
    body {
        line-height: 1.2;
    }
    </style>
    <figure style='text-align: center;'>
    <img src='' />
    <figcaption style='font-size: 0.8em; color: #888;'>Powered by Infomark</figcaption>
    </figure>
    """,
        unsafe_allow_html=True,
)

button_pressed = False

SUPPORTED_SOURCES = ["benzinga", "biztoc", "intrinio", "fmp", "tiingo"]


providers = [
    d 
    for d in list(obb.user.credentials.__dict__.keys()) 
    if obb.user.credentials.__dict__[d] is not None 
]
providers = [d.split("_")[0] for d in providers if d.split("_")[0] in SUPPORTED_SOURCES]
news_sources = [d.upper() if d == "fmp" else d.title() for d in providers]

if "news" not in st.session_state:
    st.session_state.news = None 
if "biztoc_tags" not in st.session_state:
    st.session_state.biztoc_tags = []
try:
    _all_tags = []
    _biztoc_tags = 