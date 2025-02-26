import React from "react";
import "./jsonModal.css";

function JsonModal({ isOpen, onClose, jsonData }) {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-container">
        <button onClick={onClose} className="close-btn">×</button>
        <h3>Score Groups</h3>
        <pre className="json-display">{JSON.stringify(jsonData, null, 2)}</pre>
      </div>
    </div>
  );
}

export default JsonModal;
