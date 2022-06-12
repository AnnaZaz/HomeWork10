from flask import Flask

from utils import candidates_get_all, candidates_get_by_pk, candidates_get_by_skill
from visual import build_html_for_some_candidates, build_html_for_one_candidate

app = Flask(__name__)


@app.route("/")
def index():
    candidates = candidates_get_all()
    candidates_html = build_html_for_some_candidates(candidates)
    return candidates_html


@app.route("/candidate/<int:pk>/")
def page_candidate(pk):
    candidate = candidates_get_by_pk(pk)
    if candidate is None:
        return "Такого пользователя нет"
    candidate_html = build_html_for_one_candidate(candidate)
    return candidate_html


@app.route("/skills/<skill>/")
def skill_page(skill):
    candidates = candidates_get_by_skill(skill)
    if len(candidates) == 0:
        return "Кандидата с таким навыком нет"
    candidate_html = build_html_for_some_candidates(candidates)
    return candidate_html


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
