FROM python:3.9

WORKDIR /src

COPY . .

RUN ls

RUN pwd 

RUN pip install --no-cache-dir -r requirements.txt

VOLUME /src
