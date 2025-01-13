#Dockerize the utility!
FROM python:3.9-slim

WORKDIR /app

#Copy requirements into the container
COPY requirements.txt .

# Install dependencies from file
RUN pip install --no-cache-dir -r requirements.txt

COPY AI_Virtual_Assistant.py .

CMD ["python", "AI_Virtual_Assistant.py"]