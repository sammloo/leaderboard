from app import create_app
from flask_apscheduler import APScheduler
from jobs.winner_jobs import find_and_store_winner

app = create_app()

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.add_job(
    id="find_winner_job",
    func=find_and_store_winner,
    trigger="interval",
    seconds=10,
)

if __name__ == "__main__":
    scheduler.start()
    app.run(host='0.0.0.0', port=5000)