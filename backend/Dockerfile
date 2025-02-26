FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000


RUN echo "Running Python scripts ...."


CMD ["sh", "-c", "python ./backend/populate_users.py && python ./backend/leaderboard.py"]