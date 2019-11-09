FROM python:3.7

COPY src /src

RUN pip install --upgrade pip

CMD ["python", "-m", "unittest", "discover", "-s","src/Tests"]