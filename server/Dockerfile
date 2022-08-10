FROM python:3.10-alpine
COPY server.py /app/server.py
WORKDIR /app
RUN pip install --upgrade pip && pip install fastapi uvicorn
EXPOSE 8888
CMD uvicorn server:app --reload --host 0.0.0.0 --port 8888