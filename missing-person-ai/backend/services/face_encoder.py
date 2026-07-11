import cv2
import numpy as np
from insightface.app import FaceAnalysis


class FaceEncoder:
    def __init__(self):
        self.app = FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"]
        )

        self.app.prepare(
            ctx_id=0,
            det_size=(640, 640)
        )

    def get_embedding_from_image(self, image_path):
        """
        Extract a single face embedding from an image file.
        Uses the largest detected face if multiple faces exist.
        """

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(
                f"Unable to read image: {image_path}"
            )

        faces = self.app.get(image)

        if len(faces) == 0:
            raise ValueError(
                "No face detected in image"
            )

        largest_face = max(
            faces,
            key=lambda face: (
                (face.bbox[2] - face.bbox[0]) *
                (face.bbox[3] - face.bbox[1])
            )
        )

        embedding = largest_face.embedding.astype(
            np.float32
        )

        return embedding

    def get_embedding_from_frame(self, frame):
        """
        Extract embeddings from all faces in a camera frame.
        Returns:
        [
            {
                "embedding": ...,
                "bbox": [...]
            }
        ]
        """

        faces = self.app.get(frame)

        results = []

        for face in faces:

            embedding = face.embedding.astype(
                np.float32
            )

            bbox = face.bbox.astype(
                np.int32
            )

            results.append(
                {
                    "embedding": embedding,
                    "bbox": bbox
                }
            )

        return results

    def detect_faces(self, image_path):
        """
        Returns all face bounding boxes from image.
        """

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(
                f"Unable to read image: {image_path}"
            )

        faces = self.app.get(image)

        output = []

        for face in faces:

            output.append(
                {
                    "bbox": face.bbox.astype(int).tolist()
                }
            )

        return output

    def count_faces(self, image_path):
        """
        Returns total detected faces.
        """

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(
                f"Unable to read image: {image_path}"
            )

        faces = self.app.get(image)

        return len(faces)