import re


def passwd_check(passwd):
    passwd_regexes = ('[a-z]', '[A-Z]', '[0-9]')

    if len(passwd) >= 8 and all(re.search(r, passwd) for r in passwd_regexes):
        print('Strong password!')
    else:
        print('Weak password...')


passwd_check('araezazreaezerz222ZZ')
