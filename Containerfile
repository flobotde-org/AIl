FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
EXPOSE 8000
CMD ["AIl", "run", "--port", "8000"]
