from pathlib import Path
from typing import Any, List


script_dir = Path(__file__).parent.absolute()


def read_text_file(day: int, file_name: str) -> str:
    file_path = f"{script_dir}/../data/challenge_day_{day}/{file_name}"

    with open(file_path, "r") as f:
        return f.read()


def bin_2_str(number, leading_zeros=64):
    return f"{{:0{leading_zeros}b}}".format(number)


def chunks(xs: List[Any], n: list) -> List[List[Any]]:
    n = max(1, n)
    return list(xs[i : i + n] for i in range(0, len(xs), n))
