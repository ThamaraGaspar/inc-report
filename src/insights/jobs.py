from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        return list(csv.DictReader(file))


def get_unique_job_types(path: str) -> List[str]:
    job_types = set()
    jobs = read(path)
    for job in jobs:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return list(job for job in jobs if job["job_type"] == job_type)
