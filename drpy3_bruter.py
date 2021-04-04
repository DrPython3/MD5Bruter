#!/usr/local/opt/python@3.8/bin/python3
# -*- coding: utf-8 -*-

'''
PROJECT: MD5Bruter, "Bruteforce Worker"
AUTHOR: DrPython3 @ GitHub.com
DATE: 2021-04-04
'''

# **********************
# *** PYTHON MODULES ***
# **********************

import sys
try:
    import string
    import itertools
    import hashlib
    import colorama
    from tqdm import tqdm
except:
    sys.exit('Error importing Python Modules.\n\n')

colorama.init(autoreset=True)

# ***********************************
# *** CHARSETS FOR WORD GENERATOR ***
# ***********************************

charset_letterslo = list(string.ascii_lowercase)
charset_lettersuplo = list(string.ascii_letters)
charset_digits = list(string.digits)
charset_digitsletterslo = list(string.digits) + list(string.ascii_lowercase)
charset_alphanum = list(string.ascii_letters) + list(string.digits)
charset_full = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)

# *******************
# *** BRUTEFORCER ***
# *******************

def bruter(charset_name, min_length, max_length, target_hash):
    '''
    Generates strings, calculates hashes and compares them with targeted hash.

    :param str charset_name: charset to use
    :param int min_length: min password length
    :param int max_length: max password length
    :param str target_hash: target MD5 hash
    :return: found_string, amount_tested
    '''
    amount_tested = int(0)
    found_string = str('')
    if charset_name == 'charset_letterslo':
        charset = charset_letterslo
    elif charset_name == 'charset_lettersuplo':
        charset = charset_lettersuplo
    elif charset_name == 'charset_digits':
        charset = charset_digits
    elif charset_name == 'charset_alphanum':
        charset = charset_alphanum
    elif charset_name == 'charset_digitsletterslo':
        charset = charset_digitsletterslo
    else:
        charset = charset_full
    for i in range(min_length, max_length + 1):
        print(colorama.Fore.YELLOW + f'\nTarget: {str(target_hash)}, testing strings with {str(i)} character(s) now ...')
        total = int(len(charset)**i)
        for next_string in tqdm(itertools.product(charset, repeat=i),
                                desc='progress',
                                total=total,
                                leave=False,
                                unit=' strings',
                                unit_scale=True):
                amount_tested += 1
                test_string = str('').join(next_string)
                hashed_string = hashlib.md5(test_string.encode())
                test_hash = hashed_string.hexdigest()
                if test_hash == target_hash:
                    print(colorama.Fore.GREEN + '... hit!')
                    found_string = str(test_string)
                    return found_string, str(amount_tested)
                else:
                    pass
        print(colorama.Fore.RED + '... done!')
    return found_string, str(amount_tested)
