FROM python:3.13.3

WORKDIR /code

# Corrected filename
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./summarizer.py /code/summarizer.py

CMD ["uvicorn", "summarizer:app", "--host", "0.0.0.0", "--port", "8000"]
