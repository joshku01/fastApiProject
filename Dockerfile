FROM python:3.9-slim as requirements-stage

WORKDIR /tmp

RUN pip install --upgrade pip && \
    pip install poetry

# 複製poetry 套件管理檔案
COPY ./pyproject.toml ./poetry.lock* /tmp/

# 輸出poetry 虛擬環境,用於產生requirment 二階段使用pip來建構python app
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9-alpine

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

WORKDIR /app

CMD ["python", "main.py"]