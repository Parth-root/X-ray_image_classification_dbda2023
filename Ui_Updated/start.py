import streamlit as st
import Ui
import main
from streamlit import session_state
st.set_page_config(page_title='Pneumonia Detection', page_icon=":hospital:", initial_sidebar_state='collapsed')
PAGES = {
    "Page 1": main,
    "Page 2": Ui
}

if "current_page" not in session_state:
    session_state.current_page = "Page 1"