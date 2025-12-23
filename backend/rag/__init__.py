if CI_MODE:
    self.index = None
    logger.warning("CI MODE – FAISS disabled")
elif os.path.exists(FAISS_INDEX_PATH):
    self.index = faiss.read_index(FAISS_INDEX_PATH)
    logger.info("FAISS index loaded")
else:
    self.index = None
