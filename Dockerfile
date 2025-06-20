FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install system dependencies (IMPORTANT: GIT is required for your requirements.txt)
RUN apt-get update && apt-get install -y git gcc libffi-dev libssl-dev && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
