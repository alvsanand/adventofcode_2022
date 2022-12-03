from __future__ import annotations

import heapq
from dataclasses import dataclass
from pathlib import Path

script_dir = Path(__file__).parent.absolute()


def read_text_file(day: int, file_name: str) -> str:
    file_path = f"{script_dir}/../data/challenge_day_{day}/{file_name}"

    with open(file_path, "r") as f:
        return f.read()


@dataclass
class Elf:
    total_calories: int = 0
    id: int = 1

    def add_calories(self, calories: int):
        self.total_calories += calories

    def next_elf(self) -> Elf:
        return Elf(id=self.id + 1)

    def __lt__(self, other: Elf) -> bool:
        return self.total_calories > other.total_calories


class ElfHeap(Elf):
    def __init__(self):
        self.data = []

    def push(self, elf_inventory: Elf):
        heapq.heappush(self.data, elf_inventory)

    def pop(self):
        return heapq.heappop(self.data)

    def __len__(self):
        return len(self.data)


def read_elf_inventory() -> ElfHeap:
    data = read_text_file(1, "input.txt")

    heap = ElfHeap()
    current_elf = Elf()
    to_add = False

    for line in data.splitlines():
        if line:
            try:
                current_elf.add_calories(int(line))

                to_add = True
            except Exception:
                print("Error adding calories")
        elif current_elf.total_calories > 0:
            heap.push(current_elf)
            to_add = False

            current_elf = current_elf.next_elf()

    if to_add:
        heap.push(current_elf)

    return heap
