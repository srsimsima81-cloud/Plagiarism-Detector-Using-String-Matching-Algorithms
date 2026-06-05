def generate_report(score, matches):

    report = []

    report.append("PLAGIARISM REPORT")
    report.append("=" * 40)

    report.append(f"Similarity: {score}%")
    report.append("")

    report.append("Matched Words:")

    for word in sorted(matches):
        report.append(word)

    return "\n".join(report)