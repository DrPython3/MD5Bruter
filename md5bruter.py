#!/usr/local/opt/python@3.8/bin/python3
# -*- coding: utf-8 -*-

'''
PROJECT:    MD5Bruter
AUTHOR:     DrPython3 @ GitHub.com
DATE:       2021-04-04
-------------------------------------------------------------------------------
INFO:       Bruteforce tool / cracker for MD5 hashes. Processing single hashes,
            lists and combolists (userid:md5hash). Work still in progress.
            Written just to learn more about bruteforce attacks.

            For educational purposes only!
'''

# **********************
# *** PYTHON MODULES ***
# **********************

import sys
try:
    # ... official modules:
    import os
    import colorama
    from time import sleep
    # ... custom modules:
    import drpy3_bruter as worker
    import drpy3_various as various
except:
    sys.exit('Error importing Python modules.\n\n')

# ... initialize colorama:
colorama.init(autoreset=True)

# ***************
# *** VARIOUS ***
# ***************

logo_main = str('''

.        : :::::::-.  :::::::::::::::. :::::::..    ...    :::::::::::::::.,:::::: :::::::..   
;;,.    ;;; ;;,   `';,`;;``''; ;;;'';;';;;;``;;;;   ;;     ;;;;;;;;;;;````;;;;```` ;;;;``;;;;  
[[[[, ,[[[[,`[[     [[ [[,_    [[[__[[\.[[[,/[[['  [['     [[[     [[      [[cccc   [[[,/[[['  
$$$$$$$$"$$$ $$,    $$ `""*Ycc $$""""Y$$$$$$$$c    $$      $$$     $$      $$""""   $$$$$$c    
888 Y88" 888o888_,o8P' __,od8"_88o,,od8P888b "88bo,88    .d888     88,     888oo,__ 888b "88bo,
MMM  M'  "MMMMMMMP"`   MMP"   ""YUMMMP" MMMM   "W"  "YmmMMMM""     MMM     """"YUMMMMMMM   "W" 
_______________________________________________________________________________________________
                                                                    DrPython3 @ GitHub (C) 2021

    [ OPTIONS:]          [1] = Brute Combolist   (userid:md5hash)
                         [2] = Brute Hashlist    (1x MD5-hash/line)
                         [3] = Brute MD5-hash    (single MD5-hash)
                         ==========================================
                         [0] = EXIT

''')

logo_exit = str('''
8                      8                    88 
8                      8                    88 
8oPYo. o    o .oPYo.   8oPYo. o    o .oPYo. 88 
8    8 8    8 8oooo8   8    8 8    8 8oooo8 88 
8    8 8    8 8.       8    8 8    8 8.     `' 
`YooP' `YooP8 `Yooo'   `YooP' `YooP8 `Yooo' 88 
:.....::....8 :.....::::.....::....8 :.....:...
:::::::::ooP'.::::::::::::::::::ooP'.::::::::::
:::::::::...::::::::::::::::::::...::::::::::::

... and thank you for using MD5Bruter!

If you like this tool, support my work, please.
Buy me a coffee or send a tip to one of the
following wallets:

    BTC: 19v1XuRJWoFoqqNKJ3r6wdHuRMjg2fjHji
    LTC: LbukCLWfCqUn3cu8xViQft8pDVVfDqLBZA

Every donation helps! Best wishes, DrPython3
''')

included_charsets = {
    1:'charset_letterslo',
    2:'charset_lettersuplo',
    3:'charset_digits',
    4:'charset_alphanum',
    5:'charset_full',
    6:'charset_digitsletterslo'
}

# *****************
# *** FUNCTIONS ***
# *****************

def bruteforce(type):
    '''
    For setup and starting / performing bruteforce attacks.

    :param str type: (combos / hashes / single)
    :return: None
    '''
    targets = []
    found = int(0)
    various.clean_screen()
    print(colorama.Fore.RED + '\n\n*** MD5Bruter *** Interactive Startup\n' + '='*37 + '\n\n')
    if type == 'combos' or type == 'hashes':
        target_input = str(input(colorama.Fore.WHITE + 'user@md5: enter filename, e.g. "input.txt" ...    '
                                 + colorama.Fore.YELLOW))
        try:
            targets = open(target_input, 'r').read().splitlines()
        except:
            various.clean_screen()
            print(colorama.Fore.RED + f'\n\n[ERROR] File {target_input} not found.')
            input(colorama.Fore.RED + 'Press ENTER to return to main menu.\n\n')
            return None
    elif type == 'single':
        target_input = str(input(colorama.Fore.WHITE + 'user@md5: enter hash ...    '
                                 + colorama.Fore.YELLOW))
        if target_input == '':
            print(colorama.Fore.YELLOW + '\n\nNothing entered, so returning to main menu ...')
            sleep(3.0)
            return None
        else:
            targets.append(target_input)
    else:
        various.clean_screen()
        print(colorama.Fore.RED + '\n\n[ERROR] MD5Bruter Startup failed.')
        input(colorama.Fore.RED + 'Press ENTER to return to main menu.\n\n')
        return None
    try:
        password_min = int(input(colorama.Fore.WHITE + '\n\nuser@md5: enter minimum password length, e.g. 1 ...    '
                                 + colorama.Fore.YELLOW))
        password_max = int(input(colorama.Fore.WHITE + '\n\nuser@md5: enter maximum password length, e.g. 9 ...    '
                                 + colorama.Fore.YELLOW))
        print(colorama.Fore.WHITE + '\n\nAvailable charsets:\n' + '='*19 + '\n'
              + '(1) letters (lowercase only)\n'
              + '(2) letters (lower- and uppercase)\n'
              + '(3) digits\n'
              + '(4) alphanumeric (letter and digits)\n'
              + '(5) letters, digits and symbols (full)\n'
              + '(6) lowercase letters and digits\n\n')
        charset_option = int(input(colorama.Fore.WHITE + 'user@md5: enter number of charset to use, e.g. 2 ...    '
                                   + colorama.Fore.YELLOW))
        charset = str(included_charsets[charset_option])
    except:
        print(colorama.Fore.RED + '\n\n[ERROR] Entered value not valid.\nMD5Bruter will use default values instead.\n\n')
        sleep(3.0)
        password_min = int(1)
        password_max = int(9)
        charset = str('charset_alphanum')
    try:
        bruteforce_settings = str(f'target(s): {target_input}\n'
                                  + f'total: {str(len(targets))}\n'
                                  + f'password length: {str(password_min)} - {str(password_max)}\n'
                                  + f'charset: {charset}')
        various.clean_screen()
        print(colorama.Fore.RED + '\n\n*** MD5Bruter *** Overview:\n' + '='*27)
        print(colorama.Fore.WHITE + bruteforce_settings)
        print(colorama.Fore.YELLOW + '\n\nBruteforcing started. Be patient, please (...)\n\n' + colorama.Fore.WHITE)
        various.log_startstop(str('start'))
        various.writer(bruteforce_settings + '\n')
        for next_target in targets:
            if type == 'combos':
                target = str(next_target).replace(';', ':').replace('|', ':')
                bruter_input = str(target.split(':')[1])
            else:
                bruter_input = str(next_target)
            result, amount_tries = worker.bruter(charset, password_min, password_max, bruter_input)
            if result == '':
                various.writer(str(f'[NO RESULT] {str(next_target)}, tries: {str(amount_tries)}'))
            else:
                various.writer(str(f'[RESULT] {str(next_target)}, decrypted: {str(result)}, tries: {str(amount_tries)}'))
                found += 1
        various.log_startstop(str('stop'))
        various.clean_screen()
        if found > 0:
            print(colorama.Fore.GREEN + '\n\n*** MD5Bruter *** Result:\n' + '='*25)
            print(colorama.Fore.GREEN + f'Decrypted hashes: {str(found)}, see logs.txt for details.')
            input(colorama.Fore.GREEN + 'Press ENTER to return to main menu.\n\n')
        else:
            print(colorama.Fore.RED + '\n\n*** MD5Bruter *** Result:\n' + '='*25)
            input(colorama.Fore.RED + 'No decrypted hashes.\nPress ENTER to return to main menu.\n\n')
    except:
        various.clean_screen()
        print(colorama.Fore.RED + '\n\n[ERROR] Bruteforce attack failed or has been aborted.')
        input(colorama.Fore.RED + 'Press ENTER to return to main menu.\n\n')
    return None


def md5bruter():
    '''
    Provides main menu for MD5Bruter.

    :return: None
    '''
    various.clean_screen()
    print(colorama.Fore.RED + logo_main)
    user_option = input(colorama.Fore.WHITE + 'user@md5: enter option ...    ' + colorama.Fore.YELLOW)
    if user_option == '0':
        various.clean_screen()
        print(colorama.Fore.RED + logo_exit)
        sys.exit('')
    elif user_option == '1':
        list_type = str('combos')
    elif user_option == '2':
        list_type = str('hashes')
    elif user_option == '3':
        list_type = str('single')
    else:
        various.clean_screen()
        print(colorama.Fore.YELLOW + '\n\n[INFO] No valid option entered.')
        input(colorama.Fore.YELLOW + 'Press ENTER to return to main menu.\n\n')
        return None
    try:
        bruteforce(list_type)
    except:
        pass
    return None

# ... start MD5Bruter:
while True:
    md5bruter()
