def get_content(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def get_sections(content):
    # Separate the file into two sections: instructions and levels; Furthermore get a list of stacks using the levels
    levels, instructions = [section.split("\n") for section in content.split("\n\n")]
    levels = [crate.replace("    ", " [X] ") for crate in levels[:-1]]
    levels = [[crate[1] for crate in level.split()] for level in levels]
    stacks = [[] for _ in range(len(levels[0]))]
    for level in reversed(levels):
        for index, crate in enumerate(level):
            if crate != "X":
                stacks[index].append(crate)
    return instructions, levels, stacks


def handle_move2(instruction: str, dict_stacks: dict) -> None:
    quantity, from_stack_order, to_stack_order = [
        int(i) for i in instruction.split(" ") if i.isnumeric()
    ]
    from_list = dict_stacks[from_stack_order]
    to_list = dict_stacks[to_stack_order]
    
    for i in from_list[-quantity:]:
        to_list.append(i)
    if from_list:
        del from_list[-quantity:]
    dict_stacks[to_stack_order] = to_list
    dict_stacks[from_stack_order] = from_list


def handle_move(instruction: str, dict_stacks: dict) -> None:
    quantity, from_stack_order, to_stack_order = [
        int(i) for i in instruction.split(" ") if i.isnumeric()
    ]
    from_list = dict_stacks[from_stack_order]
    to_list = dict_stacks[to_stack_order]
    for _ in range(quantity):
        to_list.append(from_list[-1])
        if from_list:
            from_list.pop(-1)
        dict_stacks[to_stack_order] = to_list
        dict_stacks[from_stack_order] = from_list


def main():
    filename = "day5/day5.txt"
    content = get_content(filename)
    instructions, levels, stacks = get_sections(content)
    print(len(levels))
    dict_stacks = {i: None for i in range(1, len(levels) + 2)}
    for i, key in enumerate(dict_stacks.keys()):
        dict_stacks[key] = stacks[i]

    # for instruction in instructions:
    #     handle_move(instruction, dict_stacks)

    for insturction in instructions:
        handle_move2(insturction, dict_stacks)

    stacklist = []
    for val in dict_stacks.values():
        stacklist.append(val[-1])
    print("".join(stacklist))


if __name__ == '__main__':
    main()