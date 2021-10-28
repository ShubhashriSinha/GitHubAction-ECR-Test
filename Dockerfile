FROM centos:latest

COPY rds-start.py .

CMD rds-start.py
