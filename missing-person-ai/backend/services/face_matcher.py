import os
import json
import faiss
import numpy as np


class FaceMatcher:
    def __init__(
        self,
        embedding_dim=512,
        index_path="database/faiss_index/persons.index",
        metadata_path="database/faiss_index/persons.json"
    ):
        self.embedding_dim = embedding_dim
        self.index_path = index_path
        self.metadata_path = metadata_path

        os.makedirs(
            os.path.dirname(self.index_path),
            exist_ok=True
        )

        if os.path.exists(self.index_path):
            self.index = faiss.read_index(
                self.index_path
            )
        else:
            self.index = faiss.IndexFlatIP(
                self.embedding_dim
            )

        if os.path.exists(self.metadata_path):
            with open(
                self.metadata_path,
                "r"
            ) as f:
                self.metadata = json.load(f)
        else:
            self.metadata = []

    def normalize_embedding(
        self,
        embedding
    ):
        embedding = np.asarray(
            embedding,
            dtype=np.float32
        )

        norm = np.linalg.norm(
            embedding
        )

        if norm == 0:
            return embedding

        return embedding / norm

    def save(self):
        faiss.write_index(
            self.index,
            self.index_path
        )

        with open(
            self.metadata_path,
            "w"
        ) as f:
            json.dump(
                self.metadata,
                f,
                indent=4
            )

    def add_person(
        self,
        person_id,
        name,
        embedding
    ):
        embedding = self.normalize_embedding(
            embedding
        )

        embedding = np.expand_dims(
            embedding,
            axis=0
        )

        self.index.add(
            embedding
        )

        self.metadata.append(
            {
                "person_id": person_id,
                "name": name
            }
        )

        self.save()

    def match_face(
        self,
        embedding,
        threshold=0.55
    ):
        if self.index.ntotal == 0:
            return None

        embedding = self.normalize_embedding(
            embedding
        )

        embedding = np.expand_dims(
            embedding,
            axis=0
        )

        distances, indices = self.index.search(
            embedding,
            1
        )

        similarity = float(
            distances[0][0]
        )

        index = int(
            indices[0][0]
        )

        if index < 0:
            return None

        if similarity < threshold:
            return None

        person = self.metadata[index]

        return {
            "person_id": person["person_id"],
            "name": person["name"],
            "similarity": round(
                similarity,
                4
            )
        }

    def total_persons(self):
        return self.index.ntotal