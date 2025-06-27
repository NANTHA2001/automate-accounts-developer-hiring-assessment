// src/api.ts
import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const uploadFile = (formData: FormData) =>
  API.post("/upload", formData);

export const validateFile = (id: number) =>
  API.post("/validate", { id });

export const processFile = (id: number) =>
  API.post("/process", { id });

export const fetchReceipts = () =>
  API.get("/receipts");

export const fetchReceiptById = (id: number) =>
  API.get(`/receipts/${id}`);
