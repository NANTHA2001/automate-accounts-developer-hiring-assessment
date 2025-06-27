// ReceiptList.tsx
import React from "react";
import { useNavigate } from "react-router-dom";
import "./ReceiptList.css";

interface Receipt {
  id: number;
  merchant_name: string;
  purchased_at: string;
  total_amount: number;
}

const ReceiptList = ({ receipts }: { receipts: Receipt[] }) => {
  const navigate = useNavigate();

  return (
    <div className="receipt-container">
      <h2>🧾 Your Receipts</h2>
      <div className="receipt-list">
        {receipts.map((receipt) => {
          const isUnknown = receipt.merchant_name === "Unknown";
          return (
            <div
              key={receipt.id}
              className={`receipt-card ${isUnknown ? "unknown" : "known"}`}
              onClick={() => navigate(`/receipts/${receipt.id}`)}
            >
              <div className="receipt-header">
                <span className="receipt-icon">{isUnknown ? "🚫" : "🏪"}</span>
                <h3>{isUnknown ? "Merchant Unknown" : receipt.merchant_name}</h3>
              </div>
              <p><span className="label">💵 Amount:</span> ₹{receipt.total_amount}</p>
              <p><span className="label">📅 Date:</span> {receipt.purchased_at === "Unknown" ? "Date Unknown" : receipt.purchased_at}</p>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default ReceiptList;
