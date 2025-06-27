import React, { useEffect, useState } from "react";
import { fetchReceiptById } from "../../axios/api.ts";
import { useParams } from "react-router-dom";
import "./ReceiptDetail.css";

const ReceiptDetail = () => {
  const { id } = useParams();
  const [receipt, setReceipt] = useState<any>(null);

  useEffect(() => {
    const load = async () => {
      if (!id) return;
      const res = await fetchReceiptById(Number(id));
      setReceipt(res.data);
    };
    load();
  }, [id]);

  if (!receipt) return <div className="loading">⏳ Loading receipt details...</div>;

  return (
    <div className="receipt-card">
      <h2>🧾 Receipt #{receipt.id}</h2>
      <div className="receipt-item">
        <span>🏪 Merchant:</span> {receipt.merchant_name}
      </div>
      <div className="receipt-item">
        <span>📅 Date:</span> {receipt.purchased_at}
      </div>
      <div className="receipt-item">
        <span>💵 Amount:</span> ₹{receipt.total_amount}
      </div>
      <div className="receipt-item">
        <span>📁 File Path:</span> {receipt.file_path}
      </div>

      <a
        className="download-button"
        href={`http://localhost:8000/${receipt.file_path}`}
        target="_blank"
        rel="noopener noreferrer"
      >
        📄 View Receipt PDF
      </a>
    </div>
  );
};

export default ReceiptDetail;
