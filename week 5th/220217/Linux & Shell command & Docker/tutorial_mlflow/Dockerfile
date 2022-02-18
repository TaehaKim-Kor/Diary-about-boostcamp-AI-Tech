FROM python:3.9-bullseye

COPY . /app
WORKDIR /app
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

RUN pip install pip==21.2.4 && \
    pip install -r pipenv.yaml

CMD ["python","train.py"]
