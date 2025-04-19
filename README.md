install python
https://www.python.org/downloads/
update environment path fot python and its Script
C:\Users\yourpcname\AppData\Local\Programs\Python\Python313\Scripts
C:\Users\yourpcname\AppData\Local\Programs\Python\Python313

install dependancies:
pip install transformers torch fastapi uvicorn

run the file

run the server
python -m uvicorn summarizer:app --host 0.0.0.0 --port 8000
