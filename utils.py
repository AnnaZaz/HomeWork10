import json

from pprint import pprint as pp

from config import DATA_PATH


def _load_data(path=DATA_PATH):
    """Загружает данные про кандидатов"""
    with open(path, 'r', encoding='utf8') as f:
        data = json.load(f)
        return data


def candidates_get_all():
    """Получает список всех кандидатов"""
    data = _load_data()
    return data


def candidates_get_by_pk(pk):
    """Получает кандидата по его pk"""
    candidates = _load_data()
    for candidate in candidates:
        if candidate['id'] == pk:
            return candidate


def candidates_get_by_skill(skill_name):
    """Получает кандидата по навыкам"""

    skilled_candidates = []
    skill_name_lower = skill_name.lower()

    candidates = _load_data()
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name_lower in skills:
            skilled_candidates.append(candidate)
            continue

    return skilled_candidates

# pp(candidates_get_by_pk(7))
