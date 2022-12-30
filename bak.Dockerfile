FROM python:3.9

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8087

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8087"]