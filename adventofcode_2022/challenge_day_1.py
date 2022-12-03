import sys

from adventofcode_2022 import read_elf_inventory


def main() -> int:
    elf_inventory = read_elf_inventory()

    fatest_elf = elf_inventory.pop()

    print(f"The elf with most calories is {fatest_elf}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
