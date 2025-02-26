from flask import Blueprint, jsonify, request
from app.models import User, Winner
import logging
from app import db
from sqlalchemy import func

user_routes = Blueprint('user_routes', __name__)

logger = logging.getLogger(__name__)

@user_routes.route('/sorted_by_scores', methods=['GET'])
def get_users_sorted_by_score():
    try:
        users = User.query.filter_by(is_deleted=False).order_by(User.points.desc()).all()
        
        users_list = [
            {
                'id': str(user.id),
                'name': user.name,
                'age': user.age,
                'points': user.points
            }
            for user in users
        ]
        
        return jsonify(users_list), 200
    except Exception as e:
        logger.error(f"Error fetching users info: {e}")
        return jsonify({"message": "An error occurred while fetching users."}), 500


@user_routes.route('/view_user/<string:user_id>', methods=['GET'])
def view_user(user_id):
    try:
        user = User.query.get(user_id)

        if not user or user.is_deleted:
            return jsonify({"message": "User not found"}), 404
        
        user_info = {
            'name': user.name,
            'age': user.age,
            'points': user.points,
            'address': user.address
        }

        return jsonify(user_info), 200

    except Exception as e:
        logger.error(f"Error viewing user: {e}")
        return jsonify({"message": "An error occurred while viewing the user."}), 500


@user_routes.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"message": "Missing data"}), 400
        
        required_field = ['name', 'age', 'address']

        for field in required_field:
            if not data.get(field):
                return jsonify({f"message": "Missing required fields: {field}"}), 400

        
        new_user = User(
            name=data.get('name'),
            age=data.get('age'),
            address=data.get('address')
        )

        db.session.add(new_user)
        db.session.commit()
        return get_users_sorted_by_score()


    except Exception as e:
        logger.error(f"Error adding user: {e}")
        return jsonify({"message": "An error occurred while adding the user."}), 500


@user_routes.route('/delete_user/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)

        if not user or user.is_deleted:
            return jsonify({"message": "User not found"}), 404

        user.is_deleted = True
        db.session.commit()

        return jsonify({"message": f"User {user_id} deleted successfully"}), 200

    except Exception as e:
        logger.error(f"Error deleting user: {e}")
        return jsonify({"message": "An error occurred while deleting the user."}), 500

@user_routes.route('/update_score/<string:user_id>', methods=['PATCH'])
def update_score(user_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"message": "Missing data"}), 400

        if not data.get('points'):
            return jsonify({"message": "Missing required field: points"}), 400

        user = User.query.get(user_id)

        if not user or user.is_deleted:
            return jsonify({"message": "User not found"}), 404

        user.points += data.get("points")
        db.session.commit()

        return get_users_sorted_by_score()

    except Exception as e:
        logger.error(f"Error updating score: {e}")
        return jsonify({"message": "An error occurred while updating the score."}), 500

@user_routes.route('/grouped_by_scores', methods=['GET'])
def get_users_grouped_by_score():
    try:
        users = db.session.query(User.points, func.array_agg(User.name), func.avg(User.age)) \
                          .filter(User.is_deleted == False) \
                          .group_by(User.points) \
                          .all()

        grouped_users = {
            score: {
                "names": names,
                "average_age": round(avg_age) if avg_age is not None else None
            }
            for score, names, avg_age in users
        }

        return jsonify(grouped_users), 200
    except Exception as e:
        logger.error(f"Error fetching scores group info: {e}")
        return jsonify({"message": "An error occurred while fetching users."}), 500

@user_routes.route('/winner', methods=['GET'])
def get_winners():
    try:
        winner = Winner.query.order_by(Winner.timestamp.desc()).limit(1).first()

        winner_info = {
            "name": winner.name,
            "points": winner.points,
            "timestamp": winner.timestamp,
        }
        return jsonify(winner_info), 200
    except Exception as e:
        logger.error(f"Error fetching winner: {e}")
        return jsonify({"message": "An error occurred while fetching winner."}), 500

