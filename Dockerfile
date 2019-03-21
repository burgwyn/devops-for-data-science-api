FROM python:3.6

RUN mkdir /app

COPY requirements.txt /app/
COPY app.py /app/

WORKDIR /app/

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]