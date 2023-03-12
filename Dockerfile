FROM python:3.12-rc-alpine3.17

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT ["python"]

CMD ["app.py"]
