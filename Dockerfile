FROM python:3.8-slim

ENV FLASK_APP=app
ENV FLASK_ENV=development

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]