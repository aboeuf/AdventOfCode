def solve(input_str):
    first_secret_code = 0
    second_secret_code = 0
    dial_position = 50
    lines = input_str.split("\n")
    for line in lines:
        if len(line) == 0:
            continue
        sign = 1 if line[0] == "R" else (-1 if line[0] == "L" else 0)
        if sign == 0:
            raise ValueError(f'invalid line "{line}" (bad direction)')
        increment = int(line[1:])
        for i in range(increment):
            dial_position = (dial_position + sign) % 100
            if dial_position == 0:
                second_secret_code += 1
        if dial_position == 0:
            first_secret_code += 1
    return {
        "success": True,
        "part_one_solution": first_secret_code,
        "part_two_solution": second_secret_code,
    }
