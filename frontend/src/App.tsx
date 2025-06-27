// App.tsx
import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import UploadForm from "./components/UploadForm/UploadForm.tsx";
import ReceiptList from "./components/ReceiptList/ReceiptList.tsx";
import ReceiptDetail from "./components/ReceiptDetail/ReceiptDetail.tsx";
import { fetchReceipts } from "./axios/api.ts";

function App() {
  const [receipts, setReceipts] = useState([]);

  const loadReceipts = async () => {
    const res = await fetchReceipts();
    setReceipts(res.data);
  };

  useEffect(() => {
    loadReceipts();
  }, []);

  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={
            <>
              <UploadForm onUploadSuccess={loadReceipts} />
              <ReceiptList receipts={receipts} />
            </>
          }
        />
        <Route path="/receipts/:id" element={<ReceiptDetail />} />
      </Routes>
    </Router>
  );
}

export default App;
