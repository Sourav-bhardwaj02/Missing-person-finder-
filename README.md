# 🧍 Missing Person Tracker AI

An AI-powered Missing Person Tracker that helps locate missing individuals by comparing uploaded images with live camera feeds using face recognition. The system is designed for environments like railway stations, airports, malls, and public places.

---

## 🚀 Features

- 📷 Upload 2–3 images of a missing person
- 🤖 AI-powered face recognition using InsightFace
- 🎥 Live CCTV/Webcam monitoring
- 🔍 Real-time face detection and matching
- 📍 Displays camera where the person is detected
- 📊 Confidence score for each match
- 🌐 Modern React frontend
- ⚡ FastAPI AI service
- 🛠 Express.js backend

---

## 🏗 Tech Stack

### Frontend
- React
- TypeScript
- Vite
- Tailwind CSS
- Axios

### Backend
- Node.js
- Express.js
- Multer
- PostgreSQL

### AI Service
- Python
- FastAPI
- InsightFace
- OpenCV
- FAISS
- NumPy
- Uvicorn

---

## 📂 Project Structure

```text
missing-person-tracker/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── routes/
│   ├── controllers/
│   ├── uploads/
│   └── package.json
│
├── ai-service/
│   ├── app.py
│   ├── tracker.py
│   ├── requirements.txt
│   └── embeddings/
│
└── README.md
```

---

## ⚙ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/missing-person-tracker.git
cd missing-person-tracker
```

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Runs on:

```
http://localhost:5173
```

---

## Backend Setup

```bash
cd backend
npm install
npm run dev
```

Runs on:

```
http://localhost:5000
```

---

## AI Service Setup

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start AI Server

```bash
uvicorn app:app --reload
```

Runs on

```
http://localhost:8000
```

---

## 🔄 Workflow

1. User uploads multiple images of the missing person.
2. Backend stores the uploaded images.
3. AI extracts facial embeddings using InsightFace.
4. Live camera frames are processed continuously.
5. Faces detected in the stream are compared with stored embeddings.
6. If a match is found above the confidence threshold, the system reports:
   - Camera ID
   - Confidence Score
   - Timestamp

---

## 📦 API Endpoints

### Upload Images

```http
POST /api/upload
```

### Start Tracking

```http
POST /api/track
```

### Stop Tracking

```http
POST /api/stop
```

### Tracking Status

```http
GET /api/status
```

---

## 📸 Screenshots

Add screenshots here.

```
Frontend Dashboard
Image Upload
Live Camera Feed
Detection Result
```

---

## 🔮 Future Improvements

- Multi-camera support
- Railway CCTV integration
- Email/SMS alerts
- GPS-based location mapping
- Mobile application
- Person re-identification
- Crowd analytics
- Admin dashboard

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sourav Bhardwaj**

GitHub: https://github.com/Sourav-bhardwaj02

Portfolio: https://web-os-portfolio-xi.vercel.app
,.
