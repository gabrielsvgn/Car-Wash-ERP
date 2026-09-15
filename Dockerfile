FROM python:3.14-slim
WORKDIR /autoerp
RUN groupadd dev && useradd -r -g dev appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chown -R appuser:dev /autoerp
USER appuser
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]