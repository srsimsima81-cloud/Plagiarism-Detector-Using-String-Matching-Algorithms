def calculate_similarity(original, submitted):

    original_words = set(original.split())

    submitted_words = set(submitted.split())

    common = original_words.intersection(submitted_words)

    score = (
        len(common) /
        len(original_words)
    ) * 100

    return round(score, 2), common