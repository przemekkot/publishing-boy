FROM python:3.6-slim

COPY . /srv

RUN pip install -r requirements.txt
RUN pip install -e .

WORKDIR /srv

VOLUME ['/srv/input']
VOLUME ['/srv/content']

CMD publishing_bot /srv/input /srv/content