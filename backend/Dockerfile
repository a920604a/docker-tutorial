FROM python:3.9-slim

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

RUN apt-get update && apt-get install -y build-essential cmake


WORKDIR /app
COPY requirements.txt .
RUN pip install opencv-python-headless

RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
