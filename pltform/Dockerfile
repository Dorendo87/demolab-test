FROM python:3.7.3-alpine

COPY . .

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 5001/tcp

ENTRYPOINT ["python"]
CMD ["pltform.py"]
