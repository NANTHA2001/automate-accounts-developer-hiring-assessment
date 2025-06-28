# 🧾 Automate Accounts – Receipt OCR System

A complete full-stack web application to **automatically extract data from scanned receipt PDFs** using OCR (Optical Character Recognition) and store the results in a structured database.

> ✅ Built as part of the **Automate Accounts Developer Hiring Assessment**.

---

## 📦 Tech Stack

| Layer     | Tech                          |
|-----------|-------------------------------|
| Frontend  | React.js + TypeScript         |
| Backend   | FastAPI (Python)              |
| OCR       | Tesseract via `pytesseract`   |
| Database  | SQLite (via SQLAlchemy ORM)   |

---

## ✨ Features

- 📤 Upload scanned receipt PDFs
- ✅ Validate uploaded files as valid PDFs
- 🧠 Extract merchant name, purchase date, total amount using OCR
- 🛑 Prevent duplicate entries based on filename
- 🔁 Reprocess all files via admin/dev API
- 🔍 View all receipts and their details via frontend
- 🧾 Stylish React UI with clear feedback

---

## 🗂️ Project Structure

automate-accounts-developer-hiring-assessment/
│
├── backend/
│   ├── app/
│   │   ├── endpoints/
│   │   │   ├── upload.py
│   │   │   ├── validate.py
│   │   │   ├── process.py
│   │   │   ├── receipts.py
│   │   │   └── dev_tools.py
│   │   ├── core/
│   │   │   └── ocr_utils.py
│   │   ├── db/
│   │   │   ├── models.py
│   │   │   ├── session.py
│   │   │   └── __init__.py
│   │   ├── main.py              
│   │   └── __init__.py
│   ├── uploaded_receipts/        
│   ├── receipts.db               
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── UploadForm.tsx
│   │   │   ├── ReceiptList.tsx
│   │   │   └── ReceiptDetail.tsx
│   │   ├── axios/
│   │   │   └── api.ts
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── package.json
│   └── tsconfig.json
│
├── .gitignore
└── README.md



## 🔌 API Endpoints

### `POST /upload`
Upload a receipt PDF.

**Request:** `multipart/form-data` with key `file`  
**Response:**
```json
{ "message": "File uploaded", "id": 1 }
POST /validate
Check if the uploaded file is a valid PDF.

Request:

json
Copy
Edit
{ "id": 1 }
Response:

json
Copy
Edit
{ "message": "File is valid PDF" }
POST /process
Run OCR on the receipt and extract data.

Request:

json
Copy
Edit
{ "id": 1 }
Response:

json
Copy
Edit
{ "message": "Receipt processed" }
GET /receipts
Fetch list of all receipts.

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "merchant_name": "Best Buy",
    "purchased_at": "12/02/21 20:35",
    "total_amount": 196.03,
    "file_path": "uploaded_receipts/receipt1.pdf"
  }
]
GET /receipts/{id}
Get details for a specific receipt.

Response:

json
Copy
Edit
{
  "id": 1,
  "merchant_name": "Best Buy",
  "purchased_at": "12/02/21 20:35",
  "total_amount": 196.03,
  "file_path": "uploaded_receipts/receipt1.pdf"
}
POST /reprocess-all
Developer utility to re-run OCR on all previously uploaded valid PDFs.

Automatically updates existing records (avoids duplicates)

🧠 Application Flow
User uploads PDF via frontend

File is saved to uploaded_receipts/

/validate checks if it's a valid PDF

/process runs OCR to extract:

Merchant name

Date & Time

Total amount

Extracted data is stored in receipts.db

UI fetches and displays all receipts

💡 Duplicate Handling
When uploading the same PDF again:

The backend checks file_path

If already processed, it updates the data instead of inserting a duplicate

This also applies when using /reprocess-all.

❌ Error Handling
Error Message	Cause
"Only PDF files are allowed"	File is not a PDF
"Invalid or missing file"	File doesn't exist or isn't valid
"Something went wrong"	Generic catch for OCR or DB errors

🧾 Frontend UI Components

Component	Purpose:

1.UploadForm.tsx	Handles file upload and shows status
2.ReceiptList.tsx	Lists all receipts with clickable entries
3.ReceiptDetail.tsx	Detailed info of a single receipt

// css
Built with React and styled with clean minimal CSS

Status messages in green/red

Uses emojis and spacing to enhance clarity

Clickable items are highlighted on hover


🧪 How to Run the Project
📦 Prerequisites
Python 3.8+

Node.js 18+

tesseract-ocr installed

✅ On Ubuntu:

sudo apt update
sudo apt install tesseract-ocr

🛠 Backend Setup (FastAPI)

1.cd backend
2.python3 -m venv venv
3.source venv/bin/activate

4.pip install -r requirements.txt

# Run the server
5.uvicorn app.main:app --reload
6.Runs at: http://localhost:8000

⚛️ Frontend Setup (React)

1.cd frontend
2.npm install
3.npm start
4.Runs at: http://localhost:3000

🧪 Testing the App

Start both backend and frontend with two terminal

1.Go to http://localhost:3000

2.Upload a valid .pdf receipt

3.Wait for "✅ Upload, validate, and process complete!"

4.View all receipts listed below the form

5.Click any to view full detail page


## 🧑‍💻 Author

Built by **[Nantha Kumar G](https://www.linkedin.com/in/nantha-kumar-g-70b09a192)** as part of the **Automate Accounts Developer Hiring Challenge**.

- 🔗 GitHub: [github.com/NANTHA2001](https://github.com/NANTHA2001)
- 🔗 LinkedIn: [linkedin.com/in/nantha-kumar-g-70b09a192](https://www.linkedin.com/in/nantha-kumar-g-70b09a192)
