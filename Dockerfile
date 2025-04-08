FROM python:3.10-slim
WORKDIR /main
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
RUN mkdir -p model
EXPOSE 8060
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8060"]