def pretty_print_result(relationship: str):
    print(f"The relationship between the sets is: {relationship}")

def load_sets_from_file(file_path: str) -> tuple[set, set]:
    set_a = set()
    set_b = set()

    with open(file_path, 'r') as file:
        for line in file:
            if "set_a" in line:
                set_a = set(map(int, line.strip().split(":")[1].split(",")))
            elif "set_b" in line:
                set_b = set(map(int, line.strip().split(":")[1].split(",")))

    return set_a, set_b
