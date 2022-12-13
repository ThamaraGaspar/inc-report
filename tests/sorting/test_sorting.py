from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    file = [
            {
                "max_salary": 4000,
                "min_salary": 2000,
                "date_posted": "2022-05-10",
                "title": "Front end developer"
            },
            {
                "max_salary": 6000,
                "min_salary": 3000,
                "date_posted": "2021-01-01",
                "title": "Back end developer"
            },
            {
                "max_salary": 8000,
                "min_salary": 4000,
                "date_posted": "2022-09-09",
                "title": "Full stack developer"
            },
    ]
    sort_by(file, "max_salary")
    assert file[0]["title"] == "Full stack developer"
    assert file[-1]["title"] == "Front end developer"

    sort_by(file, "min_salary")
    assert file[0]["title"] == "Front end developer"
    assert file[-1]["title"] == "Full stack developer"
