FROM python:3

WORKDIR /notes

COPY requirements.txt requirements.txt

#RUN apt-get install wkhtmltopdf

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "./web.py" ]