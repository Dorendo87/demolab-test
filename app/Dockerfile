FROM python:3.7.3-alpine

COPY . .

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 5000/tcp

ENTRYPOINT ["python"]
CMD ["start.py"]
