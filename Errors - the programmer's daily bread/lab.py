""" Reading ints safety."""


def read_int(prompt, min, max):
    prompt = input(prompt)
    try:
        assert min <= int(prompt) <= max
        return prompt
    except ValueError:
        return "Error: wrong input"
    except AssertionError:
        return f"Error: the value is not within permitted range ({min}..{max})"


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
