FROM python:latest
WORKDIR /usr/src/myapp
COPY myapp.py .
CMD ["python", "myapp.py"]