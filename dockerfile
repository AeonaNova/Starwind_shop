FROM python:3.11-slim

RUN mkdir /main

WORKDIR main

COPY . /main

RUN pip install -r requirements.txt

EXPOSE 8000:8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]