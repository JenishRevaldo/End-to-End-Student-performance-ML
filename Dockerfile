FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]
