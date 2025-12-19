FROM python:3.13.11-alpine3.23

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT ["python"]

CMD ["app.py"]
