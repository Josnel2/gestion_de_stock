FROM python:3.12.5

ENV PYTHONBUFFERS 1

ENV PYTHONDONTWRTEBYTECODE 1

RUN mkdir/app

WORKDIR /app

COPY . /app

RUN python -m venv /env

ENV paths /env/scripts:$PATH

RUN -m pip install --upgrade pip

COPY entrypoint.sh /app/entrypoint.sh

COPY requirements.txt /app/

RUN pip install -r requirements.txt
