FROM python:3.6

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8081

ENV NAME App

CMD ["python3", "main.py"]