FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY runtime-service.py .
EXPOSE 8090
CMD ["uvicorn", "runtime-service:app", "--host", "0.0.0.0", "--port", "8090"]
