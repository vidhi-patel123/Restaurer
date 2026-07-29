FROM python:3.14

WORKDIR / app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]

