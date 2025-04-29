# CPSC 323 Project 2

# Parsing Table (as a dictionary)
parsing_table = {
    ('E', '('): ['T', 'Q'],
    ('E', 'a'): ['T', 'Q'],

    ('Q', '+'): ['+', 'T', 'Q'],
    ('Q', '-'): ['-', 'T', 'Q'],
    ('Q', ')'): ['ε'],
    ('Q', '$'): ['ε'],

    ('T', '('): ['F', 'R'],
    ('T', 'a'): ['F', 'R'],

    ('R', '+'): ['ε'],
    ('R', '-'): ['ε'],
    ('R', '*'): ['*', 'F', 'R'],
    ('R', '/'): ['/', 'F', 'R'],
    ('R', ')'): ['ε'],
    ('R', '$'): ['ε'],

    ('F', '('): ['(', 'E', ')'],
    ('F', 'a'): ['a']
}

def predictive_parse(input_string):
    stack = ['$','E']
    input_list = list(input_string)
    index = 0

    print("Input:", input_string)
    print("Stack:", stack)
    
    
    while len(stack) > 0:
        top = stack[-1]
        current_input = input_list[index]

        if top == current_input == '$':
            print("Stack:", stack)
            print("Output: String is accepted/valid.")
            return

        elif top == current_input:
            stack.pop()
            index += 1
            print("Match:", current_input)
            print("Stack:", stack)

        elif (top, current_input) in parsing_table:
            stack.pop()
            production = parsing_table[(top, current_input)]
            if production[0] != 'ε':
                stack.extend(reversed(production))
            print(f"Apply production: {top} -> {' '.join(production)}")
            print("Stack:", stack)

        else:
            print("Stack:", stack)
            print("Output: String is not accepted/invalid.")
            return

    print("Output: String is not accepted/invalid.")

if __name__ == "__main__":
    test_inputs = ["(a+a)*a$", "a*(a/a)$", "a(a+a)$"]

    for test in test_inputs:
        print("\n========================")
        predictive_parse(test)
        print("========================\n")

    # Uncomment below if you want user input instead:
    # user_input = input("Enter a string to parse (must end with $): ")
    # predictive_parse(user_input)
