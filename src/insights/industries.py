from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    industries_list = set()
    for industrie in jobs:
        if industrie["industry"]:
            industries_list.add(industrie["industry"])
    return industries_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return list(job for job in jobs if job["industry"] == industry)
