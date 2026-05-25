FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
LABEL org.opencontainers.image.source=https://github.com/daravorobeva004-wq/git
COPY bot.py .
CMD ["python", "bot.py"]
