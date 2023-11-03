# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster
ADD . /resnet
WORKDIR /resnet

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt torch torchvision --extra-index-url https://download.pytorch.org/whl/cpu

# copy every content from the local file to the image
COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1137"]