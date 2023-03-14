FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip3 install -r ./requirements.txt --no-cache-dir

COPY .. .

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "menu_project.asgi:application"]