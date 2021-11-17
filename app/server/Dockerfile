# pull the official base image
FROM python:3.9

# set work directory
WORKDIR /srv/app/qr

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /srv/app/qr
RUN pip install -r requirements.txt

# copy project
COPY . /srv/app/qr

#EXPOSE 8000

CMD ["gunicorn", "qr.wsgi:application", "--bind", "0.0.0.0:8000"]