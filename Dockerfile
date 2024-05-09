FROM python:3.12

WORKDIR /app

COPY ./requirements.txt /app/
RUN mkdir /app/conf
RUN pip install -r requirements.txt

COPY ./*.py /app/
COPY ./network.json /app/conf/ 
VOLUME /app/conf
CMD ["python","traffic_generator.py"]
