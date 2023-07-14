FROM python:3.11.4-slim-buster

RUN mkdir -p /app
COPY . main.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora
COPY .  .
EXPOSE 7000
CMD  ["main.py"]
ENTRYPOINT [ "python" ]