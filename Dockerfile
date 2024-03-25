FROM python:3.10-alpine

WORKDIR /text

COPY requirements.txt /text/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY text /code/app

CMD ["poetry", "run"]
