FROM python:3
COPY ./ engagement-monitor
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
# RUN mkdir engagement-monitor
WORKDIR /engagement-monitor
RUN python manage.py makemigrations 
RUN python manage.py migrate
EXPOSE 8000
CMD gunicorn engagement.wsgi --bind 0.0.0.0:8000
