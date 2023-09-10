FROM python:3.11
COPY . /user/app

WORKDIR /user/app
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install fontconfig
RUN pip install -r requirements.txt


EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
