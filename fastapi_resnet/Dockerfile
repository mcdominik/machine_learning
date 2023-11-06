# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster
ADD . /resnet
WORKDIR /resnet

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir torch==1.13.1+cpu torchvision==0.14.1+cpu --extra-index-url https://download.pytorch.org/whl/cpu

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1137"]