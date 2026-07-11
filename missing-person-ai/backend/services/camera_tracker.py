import cv2

from services.face_encoder import FaceEncoder
from services.face_matcher import FaceMatcher


class CameraTracker:
    def __init__(self):
        self.encoder = FaceEncoder()
        self.matcher = FaceMatcher()

    def start_tracking(
        self,
        camera_index=0,
        threshold=0.55
    ):
        cap = cv2.VideoCapture(camera_index)

        if not cap.isOpened():
            raise Exception(
                "Unable to open camera"
            )

        cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            640
        )

        cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            480
        )

        print(
            "\nTracking Started..."
        )

        print(
            "Press Q to quit\n"
        )

        while True:
            success, frame = cap.read()

            if not success:
                continue

            faces = self.encoder.get_embedding_from_frame(
                frame
            )

            for face in faces:

                bbox = face["bbox"]

                x1, y1, x2, y2 = bbox

                result = self.matcher.match_face(
                    face["embedding"],
                    threshold
                )

                if result:

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    text = (
                        f'{result["name"]} '
                        f'({result["similarity"]})'
                    )

                    cv2.putText(
                        frame,
                        text,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2
                    )

                else:

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 0, 255),
                        2
                    )

                    cv2.putText(
                        frame,
                        "Unknown",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 0, 255),
                        2
                    )

            cv2.imshow(
                "Missing Person Tracker",
                frame
            )

            key = cv2.waitKey(1)

            if key & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()