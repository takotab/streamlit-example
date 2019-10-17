from python:3.7

COPY req.txt req.txt
RUN pip install -r req.txt

COPY app app/
COPY streamlit_overview.py streamlit_overview.py
COPY start_streamlit.sh start_streamlit.sh
COPY api_token.json api_token.json

EXPOSE 8501

COPY main.py main.py
CMD ["bash","start_streamlit.sh"]
# CMD ["python3", "main.py"]