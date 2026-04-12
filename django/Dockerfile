FROM python

WORKDIR /app

COPY project/requirements.txt .
RUN pip install -r requirements.txt

COPY project .

# CMD para producción con Gunicorn
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn project.wsgi:application --bind 0.0.0.0:$PORT"]