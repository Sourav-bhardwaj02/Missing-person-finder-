import os
import uuid
import threading

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from services.face_encoder import FaceEncoder
from services.face_matcher import FaceMatcher
from services.camera_tracker import CameraTracker


app = FastAPI(
    title="Missing Person Tracker API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

encoder = FaceEncoder()
matcher = FaceMatcher()


@app.get("/")
def root():
    return {
        "message": "Missing Person Tracker Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "persons_registered": matcher.total_persons()
    }


@app.get("/persons")
def get_persons():
    return {
        "count": len(matcher.metadata),
        "persons": matcher.metadata
    }


@app.post("/upload-person")
async def upload_person(
    name: str = Form(...),
    file: UploadFile = File(...)
):
    try:

        person_id = str(
            uuid.uuid4()
        )

        extension = os.path.splitext(
            file.filename
        )[1]

        image_path = os.path.join(
            UPLOAD_DIR,
            f"{person_id}{extension}"
        )

        with open(
            image_path,
            "wb"
        ) as buffer:
            buffer.write(
                await file.read()
            )

        embedding = encoder.get_embedding_from_image(
            image_path
        )

        matcher.add_person(
            person_id=person_id,
            name=name,
            embedding=embedding
        )

        return {
            "success": True,
            "person_id": person_id,
            "name": name,
            "image_path": image_path
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


def run_tracker():
    tracker = CameraTracker()
    tracker.start_tracking()


@app.post("/start-tracking")
def start_tracking():

    try:

        tracking_thread = threading.Thread(
            target=run_tracker,
            daemon=True
        )

        tracking_thread.start()

        return {
            "success": True,
            "message": "Tracking started"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


@app.get("/stats")
def stats():

    return {
        "registered_persons":
            matcher.total_persons()
    }