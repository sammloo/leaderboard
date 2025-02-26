import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def find_and_store_winner():
    from leaderboard import app
    from app import db
    from app.models import User, Winner

    with app.app_context():
        logger.info("Running scheduled job: Finding winner...")

        try:
            max_points_user = db.session.query(User).order_by(User.points.desc()).first()
            if max_points_user:
                tied_users = db.session.query(User).filter(User.points == max_points_user.points).all()

                if len(tied_users) == 1:
                    winner = Winner(user_id=max_points_user.id, name=max_points_user.name, points=max_points_user.points)
                    db.session.add(winner)
                    db.session.commit()
                    logger.info(f"Winner declared: {max_points_user.name} at {datetime.utcnow()}")
                else:
                    logger.info("Tie detected, no winner declared.")
            else:
                logger.info("No users found.")
        except Exception as e:
            logger.error(f"Error finding winner: {e}")
