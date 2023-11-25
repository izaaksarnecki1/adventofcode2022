def get_content(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    filename = "day4/day4.txt"
    content = get_content(filename).splitlines()

    counter = 0
    for elf in content:
        if get_ranges(elf):
            counter += 1

    print(counter)


def get_ranges(vals: str) -> bool:
    val1, val2 = [[int(x) for x in vals.split("-")] for vals in vals.split(",")]
    min1, max1 = min(val1), max(val1)
    min2, max2 = min(val2), max(val2)
    if (min1 <= min2 and max1 >= max2) or (min2 <= min1 and max2 >= max1):
        return True
    elif min1 <= min2 and max1 >= min2 or min1 <= max2 and max1 >= max2:
        return True
    else:
        return False


main()
