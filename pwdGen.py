import random
import string

'''=-=-=--=-=-=-=--=-=-=-=--=-=-=-=-=-=-=-=-=-=-Password-Generator-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-
'pwdGen.py' is meant to help ease the stress of choosing a new secure* password. With 'pwdGen.py' you can input
exactly how long the generated password will be, along with if it should contain numbers, and/or special characters. In the
future 'pwdGen.py' may be updated and configured to encrypt/store the randomly generated passwords; So that the user
does not forget them.
'''


def gen_pass(min_len, numbers=True, spec_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    chars = letters
    if numbers:
        chars += digits
    if spec_chars:
        chars += special

    pwd = ""
    meet_criteria = False
    has_num = False
    has_spec = False

    while not meet_criteria or len(pwd) < min_len:
        new_char = random.choice(chars)
        pwd += new_char

        if new_char in digits:
            has_num = True
        elif new_char in special:
            has_spec = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_num
        if spec_chars:
            meet_criteria = meet_criteria and has_spec

    return pwd


min_length = int(input("Enter the Minimum Length of the Password: "))
has_numb = input("Do you want to have numbers(y/n)? ").lower() == 'y'
has_specs = input("Do you want to have Special Characters(y/n)? ").lower() == 'y'
gen_pwd = gen_pass(min_length, has_numb, has_specs)
print("Generated Password: ", gen_pwd)

