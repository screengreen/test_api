FROM python:3.10-slim

COPY . .

RUN pip install -r requirements.txt

CMD ['uvicorn', 'fastapi_t:app', '--host', '0.0.0.0', '--post', '80']

