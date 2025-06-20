FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install system dependencies first
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]  # Change "main.py" if your main file is different
