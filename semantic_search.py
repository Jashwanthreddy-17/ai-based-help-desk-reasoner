from sentence_transformers import (
    SentenceTransformer,
    util
)

# Small fast model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def find_best_match(
    user_query,
    kb_articles
):

    issues = [
        article.issue
        for article in kb_articles
    ]

    if not issues:
        return None

    issue_embeddings = model.encode(
        issues,
        convert_to_tensor=True
    )

    query_embedding = model.encode(
        user_query,
        convert_to_tensor=True
    )

    similarities = util.cos_sim(
        query_embedding,
        issue_embeddings
    )[0]

    best_score = similarities.max().item()

    best_index = (
        similarities.argmax().item()
    )

    return (
        kb_articles[best_index],
        best_score
    )