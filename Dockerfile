FROM python:3.9
COPY . /user/app 

WORKDIR /user/app
COPY . .

# install dependencies  
RUN pip install --upgrade pip
RUN apt-get update 
RUN apt-get install fontconfig
RUN pip install -r dev-requirements.txt 


EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
