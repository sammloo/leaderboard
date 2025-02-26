# Leaderboard

## Overview

This is a full-stack web application for a leaderboard, designed to track scores for different users and generate winners. It is built using:

- **Frontend:** React, Vite
- **Backend:** Python, Flask
- **Database:** PostgreSQL

## Features

- 🏆 Generate random users starting with 0 points
- 📈 Increment and decrement user scores
- ➕➖ Add or remove users
- 🔍 View user details by clicking their name
- 📊 Group users by scores
- ⏳ Auto-generate winner record every 5 minutes

## Installation

### Prerequisites

Ensure you have the following installed:

- Node.js
- Docker

### Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/sammloo/leaderboard.git
   cd leaderboard
   ```

2. Start the backend server using Docker:  
    _Ensure `INIT_DB=true` is set in `docker-compose.yml` for generating random users._

   ```sh
   docker-compose up --build
   ```

   The backend service runs at: `http://127.0.0.1:5001`

3. Check health of the backend server

   ```sh
   curl http://127.0.0.1:5001/health
   ```

   Expected message:

   ```sh
   The server is healthy
   ```

4. Start the frontend server

   ```sh
   CD frontend
   npm install
   npm run dev
   ```

   You can now access the app at: `http://localhost:5173/`

## API Documentation

The backend provides a RESTful API. You can test the endpoints using Postman or `curl`.

### Example Endpoints

- `GET /health` - Check the health of the server
- `GET /users/sorted_by_scores` - Fetch all users data sorted by scores
- `GET /users/view_user/<string:user_id>` - Fetch details information for a specific user
- `POST /users/add_user` - Add an new user
- `DELETE /users/delete_user/<string:user_id>` - Delete a specitic user
- `PATCH /users/update_score/<string:user_id>` - Update scores for a specific user
- `GET /users/grouped_by_scores` - Fetch users information grouped by scores
- `GET /users/winner` - Fetch the lastest winner

## Contact

For questions or issues, please create an issue in the repository.
