FROM python:3.8-slim

WORKDIR /backEnd

COPY ./requirements.txt /backEnd/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backEnd/requirements.txt

COPY ./data_store  /backEnd/data_store
COPY ./src  /backEnd/src



CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0" ,"--port", "10000"]

