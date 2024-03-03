def eval_loop():
    result = None
    while True:
        user_input = input("Input: ")
        if user_input == 'done':
            break
        try:
            result = eval(user_input)
            print(result)
        except (NameError, SyntaxError) as e:
            print(e)
    return result

import math  # in case you need to evaluate some complex functions
eval_loop()
