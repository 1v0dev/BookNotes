FROM python:3

WORKDIR /notes

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends xvfb wkhtmltopdf

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "./web.py" ]