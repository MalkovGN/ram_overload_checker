FROM python:3.10.12-slim

WORKDIR /docusketch

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/sh"]
