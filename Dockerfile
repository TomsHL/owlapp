FROM python:3.8.12-buster

RUN pip install --upgrade pip

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY owlapp /owlapp

CMD uvicorn owlapp.fast:app --reload --host 0.0.0.0 --port 8000
