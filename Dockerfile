FROM python:3.6-slim

COPY . /srv
WORKDIR /srv


RUN apt -y update;apt -y install git
RUN git config --global user.email "publishing-boy@dayan.com"
RUN git config --global user.name "Publishing Boy"


RUN pip install -r requirements.txt
RUN pip install -e .

VOLUME ['/srv/input']
VOLUME ['/srv/content']

CMD publishing_bot /srv/input /srv/content
