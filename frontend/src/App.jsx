import { useState, useEffect } from "react";
import "./App.css";
import UserModal from "./modals/userModal";
import JsonModal from "./modals/jsonModal";

const BACKEND_ENDPOINT = "http://127.0.0.1:5001";

function App() {
  const [users, setUsers] = useState([]);
  const [isUserModalOpen, setIsUserModalOpen] = useState(false);
  const [isJsonModalOpen, setIsJsonModalOpen] = useState(false);
  const [jsonData, setJsonData] = useState(null);
  const [selectedUser, setSelectedUser] = useState(null);
  const [winner, setWinner] = useState({});

  useEffect(() => {
    fetch(`${BACKEND_ENDPOINT}/users/sorted_by_scores`)
      .then((response) => response.json())
      .then((data) => setUsers(data))
      .catch((error) => console.error("Error fetching users:", error));
  }, []);

  const updatePoints = (id, points) => {
    fetch(`${BACKEND_ENDPOINT}/users/update_score/${id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ points }),
    })
      .then((response) => response.json())
      .then((sortedUsers) => setUsers(sortedUsers))
      .catch((error) => console.error("Error updating scores", error));
  };

  const removeUser = (id) => {
    fetch(`${BACKEND_ENDPOINT}/users/delete_user/${id}`, { method: "DELETE" })
      .then((response) => {
        if (!response.ok) throw new Error("Failed to delete user");
        setUsers((prevUsers) => prevUsers.filter((user) => user.id !== id));
      })
      .catch((error) => console.error("Error deleting user:", error));
  };

  const addUser = (userData) => {
    fetch(`${BACKEND_ENDPOINT}/users/add_user`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userData),
    })
      .then((response) => response.json())
      .then((newUser) => setUsers(newUser))
      .catch((error) => console.error("Error adding user:", error));
  };

  const showScoreGroups = () => {
    fetch(`${BACKEND_ENDPOINT}/users/grouped_by_scores`)
      .then((response) => response.json())
      .then((groupedData) => {
        setJsonData(groupedData);
        setIsJsonModalOpen(true);
      })
      .catch((error) => console.error("Error fetching grouped users:", error));
  };

  const selectUser = (id) => {
    fetch(`${BACKEND_ENDPOINT}/users/view_user/${id}`)
      .then((response) => response.json())
      .then((data) => {
        setSelectedUser(data);
        setIsUserModalOpen(true);
      })
      .catch((error) => console.error("Error viewing user:", error));
  };

  const showWinner = () => {
    fetch(`${BACKEND_ENDPOINT}/users/winner`)
      .then((response) => response.json())
      .then((data) => setWinner(data))
      .catch((error) => console.error("Error fetching the winner:", error));
  };

  return (
    <div className="leaderboard-container">
      {isUserModalOpen && (
        <UserModal
          isOpen={isUserModalOpen}
          onClose={() => {
            setIsUserModalOpen(false);
            setSelectedUser(null);
          }}
          onSubmit={addUser}
          data={selectedUser}
        />
      )}
      {isJsonModalOpen && (
        <JsonModal
          isOpen={isJsonModalOpen}
          onClose={() => setIsJsonModalOpen(false)}
          jsonData={jsonData}
        />
      )}

      <div className="user-list">
        {users.map((user) => (
          <div key={user.id} className="user-row">
            <button onClick={() => removeUser(user.id)} className="remove-btn">
              X
            </button>
            <div className="user-info">
              <span onClick={() => selectUser(user.id)} className="user-name">
                {user.name}
              </span>
            </div>
            <span className="points">{user.points} points</span>
            <div className="button-group">
              <button onClick={() => updatePoints(user.id, 1)} className="increment-btn">
                +
              </button>
              <button onClick={() => updatePoints(user.id, -1)} className="decrement-btn">
                -
              </button>
            </div>
          </div>
        ))}
      </div>

      <button onClick={() => setIsUserModalOpen(true)} className="add-user-btn">
        + Add User
      </button>

      <button onClick={showScoreGroups} className="add-user-btn">
        Show Score Groups
      </button>
     
      <button onClick={showWinner} className="add-user-btn">
        Show Winner
      </button>

      {winner && (
        <div className="winner">
          {winner.name && (
            <div className="winner">
              <p>{winner.name} - {winner.points} points - {winner.timestamp}</p>
           </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
