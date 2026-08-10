class RetrievalConfig:
    """
    Enterprise Retrieval Configuration

    All retrieval-related hyperparameters should
    be centralized here for easy tuning and
    environment-specific deployment.
    """

    # ==================================================
    # Search Top-K Configuration
    # ==================================================

    # Number of candidates retrieved by Vector Search
    VECTOR_TOP_K = 10

    # Number of candidates retrieved by BM25 Search
    BM25_TOP_K = 10

    # Final maximum number of retrieval results
    FINAL_TOP_K = 5

    # ==================================================
    # Hybrid Score Fusion
    # ==================================================

    # Weight of semantic vector retrieval
    VECTOR_WEIGHT = 0.7

    # Weight of BM25 lexical retrieval
    BM25_WEIGHT = 0.3

    # ==================================================
    # Score Filtering
    # ==================================================

    # Minimum hybrid score required
    MIN_HYBRID_SCORE = 0.20

    # ==================================================
    # Diversity Filter
    # ==================================================

    # Maximum number of chunks retained
    # from the same document
    MAX_CHUNKS_PER_DOCUMENT = 2

    # ==================================================
    # Dynamic Top-K
    # ==================================================

    # Minimum score required to enter
    # the final prompt
    DYNAMIC_TOP_K_MIN_SCORE = 0.55

    # Maximum chunks sent to LLM
    DYNAMIC_TOP_K_MAX = 5