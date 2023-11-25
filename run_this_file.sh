#!/bin/bash
python -m venv .venv
source .venv/bin/activate
pip install streamlit
streamlit run Ui.py --server.port 80

