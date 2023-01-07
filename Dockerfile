FROM python:3.8.0-slim

RUN apt update && apt install -y python3

COPY . .

# ENTRYPOINT ["python3"]
RUN pip install --user -r requirements.txt

CMD ["python3","/app/main.py"]
