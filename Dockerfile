FROM python:3.7.2

RUN apt-get update && apt-get upgrade -y \
    && apt-get clean

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY app.py /app/app.py

EXPOSE 5000

CMD [ "python", "app.py" ]
