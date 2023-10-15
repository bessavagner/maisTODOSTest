FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

CMD ["flask", "run", "--host=0.0.0.0"]
