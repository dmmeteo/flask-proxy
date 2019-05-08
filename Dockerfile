FROM python:3.7
ENV PYTHONUNBUFFERED 1

# Adds our application code to the image
COPY . /app
WORKDIR /app

# Allows docker to cache installed dependencies between builds
RUN pip install pipenv
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt

# Run server
ENTRYPOINT ["python"]
CMD ["app.py"]
