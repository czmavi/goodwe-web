FROM python:3.13.1-alpine3.21

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT ["python"]

CMD ["app.py"]
