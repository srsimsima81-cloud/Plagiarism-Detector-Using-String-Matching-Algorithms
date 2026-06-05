from src.preprocess import clean_text
from src.similarity import calculate_similarity
from src.report import generate_report


def read_file(path):

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


original = read_file(
    "documents/original.txt"
)

submitted = read_file(
    "documents/submitted.txt"
)

original = clean_text(original)

submitted = clean_text(submitted)

score, matches = calculate_similarity(
    original,
    submitted
)

report = generate_report(
    score,
    matches
)

print(report)

with open(
    "reports/report.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(report)

print("\nReport Saved.")