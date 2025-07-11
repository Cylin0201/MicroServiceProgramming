FROM python:latest
COPY . /app
RUN apt-get update 
RUN echo "this is a python seb server container"
CMD ["python", "/app/webserver.py"]
EXPOSE 9000