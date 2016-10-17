#!/usr/bin/python

import crypt

def main():
    crack()

def crack():

    for d inopen('shadow', 'r'):
    print d
        if '*' in d.split(':') or
'!' in d.split(':'):
            pass
        else:
            e = d.split(':')
            f = e[1].split('$')
            i = 0
            for g in
open('password.lst', 'r'):
                i = i + 1
                h =
crypt.crypt(g.strip()),
''.join(["$", f[1], "$", f[2]]),
"$"]))
                if h.split('$')[3]
                     == f