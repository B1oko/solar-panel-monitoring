FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY exporter.py exporter.py

EXPOSE 8000

CMD ["python", "exporter.py"]
