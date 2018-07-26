#!/usr/local/bin/python

import pexpect

HEADER = '\033[95m'
ENDC = '\033[0m'

print HEADER + "Spawn the shell" + ENDC
child = pexpect.spawn('./shell')
child.expect(b'\s*.*>.*\s*', timeout=2)

print HEADER + "Testing the help command" + ENDC
child.sendline('help')
child.expect(b'\s*.*>.*\s*', timeout=2)
print child.after

print HEADER + "Testing the cd to the upper folder command" + ENDC
child.sendline('cd ..')
child.expect(b'\s*.*>.*\s*', timeout=2)
child.sendline('pwd')
# Change the regex to test somewhere else
child.expect(b'\s*.*>.*\s*', timeout=2)
print child.after

print HEADER + "Testing the exit command" + ENDC
pid = child.pid
print "PID: " + str(pid)
print child.sendline('exit')
child.expect(b'^((?!>).)*$', timeout=1)
print child.after

parent = pexpect.spawn('ps ' + str(pid) + ' | wc -l')
parent.expect(b'1', timeout=1)
print "Test done"

