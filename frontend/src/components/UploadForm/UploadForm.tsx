import React, { useState } from "react";
import { uploadFile, validateFile, processFile } from "../../axios/api.ts";
import "./UploadForm.css";

interface UploadFormProps {
  onUploadSuccess: () => void;
}

const UploadForm: React.FC<UploadFormProps> = ({ onUploadSuccess }) => {
  const [file, setFile] = useState<File | null>(null);
  const [uploadStatus, setUploadStatus] = useState<string>("");

  const handleUpload = async () => {
    if (!file) {
      setUploadStatus("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const uploadRes = await uploadFile(formData);
      const id = uploadRes.data.id;

      await validateFile(id);
      await processFile(id);

      setUploadStatus("✅ Upload, validate, and process complete!");
      onUploadSuccess(); // Refresh receipt list
    } catch (err: any) {
      console.error(err);
      const message =
        err?.response?.data?.detail || "❌ Something went wrong!";
      setUploadStatus(message);
    }
  };

  return (
    <div className="upload-container">
      <h2>📤 Upload Receipt PDF</h2>
      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />
      <button onClick={handleUpload}>Upload</button>
      {uploadStatus && (
        <p
          className="status"
          style={{ color: uploadStatus.startsWith("✅") ? "green" : "red" }}
        >
          {uploadStatus}
        </p>
      )}
    </div>
  );
};

export default UploadForm;
