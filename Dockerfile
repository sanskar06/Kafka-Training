FROM python:3

RUN pip install kafka-python

COPY producer.py .

CMD ["python", "producer.py"]