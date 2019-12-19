FROM python:3.7-slim
WORKDIR /xkcd-api

ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock
RUN pip install pipenv && pipenv install --system

ADD wsgi.py wsgi.py
ADD xkcd_api xkcd_api

ADD cmd.sh cmd.sh
RUN chmod +x cmd.sh

ENTRYPOINT [ "/xkcd-api/cmd.sh" ]