FROM python:3.8-slim

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN pip install --no-deps --no-cache-dir --upgrade -r /backend/requirements.txt


COPY ./data_store  /backend/data_store
COPY ./src  /backend/src


EXPOSE 1000
CMD ["python", "server.py"]
