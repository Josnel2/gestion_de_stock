FROM python:3.12.5

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN python -m venv /env

ENV PATH="/env/bin:$PATH"

RUN python -m pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
