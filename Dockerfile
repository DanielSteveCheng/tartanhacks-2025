FROM python:3.11

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "deepclean_app.py"]
