"""My implementation of fixxbuzz."""
def fizzbuzz(number):
    print(
    "{f}{b}".format(
        f = "Fizz" if number % 3 == 0 else "",
        b = "Buzz" if number % 5 == 0 else ""))

def old_fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')

def i_take_all_the_arguments(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2 + arg3 + arg4)

i_take_all_the_arguments('hi', 1, 2, 3)
i_take_all_the_arguments('hi', 'a', 'b', 'c')
i_take_all_the_arguments(arg4=3, arg3=2, arg2=1, arg1='hi')
#i_take_all_the_arguments(100, arg1='hai', arg3=2, arg2=1)

def print_person(first, last_name, middle_name=None):
    """Prints out a person's name.

    This function prints out the person's name. It's
    kind of useless.

    Args:
        first: (str) Ths person's first name.
        last_name: (str) This person's last name.
        middle_name: (str) Optiona. This person's middle_name
    Returns:
        (str) The string of the person's name.
    """
    middle_name = middle_name or ''
    return '{f} {m} {l}'.format(
        f=first, m=middle_name, l=last_name)

print_person('Sally', 'Sue', middle_name='Anne')

"""
while True:
    human_input = input('Let me check your fizzbuzziness or say "stop": ')
    if human_input == 'stop':
        break
    fizzbuzz(human_input)
"""
