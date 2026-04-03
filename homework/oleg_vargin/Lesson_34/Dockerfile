FROM python:3
WORKDIR /app
COPY requirements.txt .
COPY step_1.py .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "step_1.py"]