FROM python:3.8

RUN pip install aiofiles aiohttp flask

COPY app4.py /app/app4.py

WORKDIR /app

CMD ["python", "app4.py"]