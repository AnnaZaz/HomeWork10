def build_html_for_one_candidate(candidate):
    candidate_for_html = f'<img src={candidate["picture"]} width="200">\n'
    candidate_for_html += f'Имя кандидата - {candidate["name"]}\n'
    candidate_for_html += f'Позиция кандидата: {candidate["position"]}\n'
    candidate_for_html += f'Навыки кандидата: {candidate["skills"]}\n'
    return f"<pre>{candidate_for_html}</pre>"


def build_html_for_some_candidates(candidates):
    candidates_for_html = ""
    for candidate in candidates:
        candidates_for_html += f'Имя кандидата - {candidate["name"]}\n'
        candidates_for_html += f'Позиция кандидата: {candidate["position"]}\n'
        candidates_for_html += f'Навыки кандидата: {candidate["skills"]}\n'
    return f"<pre>{candidates_for_html}</pre>"
