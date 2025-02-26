import React, { useState, useEffect } from "react";
import "./userModal.css";

function UserModal({ isOpen, onClose, onSubmit, data }) {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [address, setAddress] = useState("");

  useEffect(() => {
    if (data) {
      setName(data.name);
      setAge(data.age);
      setAddress(data.address);
    } else {
      setName("");
      setAge("");
      setAddress("");
    }
  }, [data]);

  const handleSubmit = () => {
    if (name && age && address) {
      onSubmit({ name, age, address });
      onClose();
    } else {
      alert("Please fill in all fields.");
    }
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-container">
        <button onClick={onClose} className="close-btn">×</button>
        <h3>{data ? "User Info" : "Add New User"}</h3>

        <label htmlFor="name" className="input-label">Name</label>
        <input type="text" className="modal-input" placeholder="Name" value={name} 
          onChange={(e) => setName(e.target.value)} disabled={!!data} />

        <label htmlFor="name" className="input-label">Age</label>  
        <input type="number" className="modal-input" placeholder="Age" value={age} 
          onChange={(e) => setAge(e.target.value)} disabled={!!data} />

        <label htmlFor="name" className="input-label">Address</label>
        <input type="text" className="modal-input" placeholder="Address" value={address} 
          onChange={(e) => setAddress(e.target.value)} disabled={!!data} />

        {!data && (
          <button onClick={handleSubmit} className="modal-btn">
            Add User
          </button>
        )}
      </div>
    </div>
  );
}

export default UserModal;
