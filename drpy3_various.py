#!/usr/local/opt/python@3.8/bin/python3
# -*- coding: utf-8 -*-

'''
PROJECT: MD5Bruter, "Various Stuff"
AUTHOR: DrPython3 @ GitHub.com
DATE: 2021-04-03
'''

# **********************
# *** PYTHON MODULES ***
# **********************

import sys
try:
    import os
    import time
except:
    sys.exit('Error importing Python modules.\n\n')

# *****************
# *** FUNCTIONS ***
# *****************

def clean_screen():
    '''
    Provides a blank screen on purpose.

    :return: None
    '''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    return None


def writer(output):
    '''
    Saves any output to textfile logs.txt.

    :param str output: any output to save
    :return: True/False
    '''
    try:
        with open('logs.txt', 'a+') as output_file:
            output_file.write(output + '\n')
    except:
        return False
    return True


def log_startstop(type):
    '''
    Writes timestamps (start, end) to log-file.

    :param str type: (start/stop)
    :return: None
    '''
    user_time = time.asctime(
        time.localtime()
    )
    if type == 'start':
        log = writer(str(
            f'MD5Bruter startet at: {str(user_time)}\n'
        ))
    else:
        log = writer(str(
            f'\nMD5Bruter stopped at: {str(user_time)}\n'
        ))
    return None
