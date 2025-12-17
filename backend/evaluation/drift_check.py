import numpy as np

def embedding_drift(old_embeddings, new_embeddings):
    """
    Cosine distance drift check
    """
    diff = np.mean(
        np.linalg.norm(old_embeddings - new_embeddings, axis=1)
    )
    return round(float(diff), 4)
