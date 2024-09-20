# official FastAPI Uvicorn image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# set wd
WORKDIR /app

# cpy reqs 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# cpy app code 
COPY . .
EXPOSE 80

# start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
