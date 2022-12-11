FROM python:3.9
RUN pip install httpx
RUN pip install FastAPI
RUN pip install "uvicorn[standard]"
RUN pip install requests

WORKDIR /app
COPY . .

CMD ["bash", "./start.sh"]
