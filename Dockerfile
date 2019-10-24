FROM python:3
COPY ./ engagement-monitor
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
# RUN mkdir engagement-monitor
WORKDIR /engagement-monitor
RUN python manage.py makemigrations 
RUN python manage.py migrate
CMD gunicorn engagement.wsgi 0.0.0.0:8000
