FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install gcc and python3-dev
RUN apt-get update && apt-get install -y gcc python3-dev

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN rm -rf staticfiles

ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}

RUN python3 manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"] 
