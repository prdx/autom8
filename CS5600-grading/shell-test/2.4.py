import pexpect
import os
import time

HEADER = '\033[95m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'
FAIL = '\033[91m'
BOLD = '\033[1m'

def test_pipe_with_spaces():
    child = pexpect.spawn('./shell')
    try:
        print BOLD + "Test pipe with spaces" + ENDC
        child.sendline('echo \"hello world\" | wc -l')
        child.expect(b'1', timeout=2)
        print OKGREEN + "SUCCESS" + ENDC
    except pexpect.TIMEOUT:
        print FAIL + "FAILED" + ENDC
    except pexpect.EOF:
        print FAIL + "FAILED" + ENDC
    child.close()

def test_pipe_without_spaces():
    child = pexpect.spawn('./shell')
    try:
        print BOLD + "Test pipe without spaces" + ENDC
        child.sendline('echo hello world|wc -l')
        child.expect(b'1', timeout=2)
        print OKGREEN + "SUCCESS" + ENDC
    except pexpect.TIMEOUT:
        print FAIL + "FAILED. Changing to interactive." + ENDC
        child.interact()
    except pexpect.EOF:
        print FAIL + "FAILED. Changing to interactive." + ENDC
        child.interact()
    child.close()

def test_output_redirection():
    child = pexpect.spawn('./shell')
    try:
        print BOLD + "Test output redirection" + ENDC
        child.sendline('echo hello world > sample.txt')
        child.sendline("cat sample.txt")
        child.expect(b'hello world', timeout=2)
        print OKGREEN + "SUCCESS" + ENDC
    except pexpect.TIMEOUT:
        print FAIL + "FAILED" + ENDC
        child.interact()
    except pexpect.EOF:
        print FAIL + "FAILED" + ENDC
        child.interact()
    child.close()

def test_input_redirection():
    child = pexpect.spawn('./shell')
    try:
        print BOLD + "Test input redirection" + ENDC
        child.sendline('wc -l < 2.4.txt')
        child.expect(b'1', timeout=2)
        print OKGREEN + "SUCCESS" + ENDC
    except pexpect.TIMEOUT:
        print FAIL + "FAILED" + ENDC
        child.interact()
    except pexpect.EOF:
        print FAIL + "FAILED" + ENDC
        child.interact()
    child.close()

def test_multiple_commands():
    child = pexpect.spawn('./shell')
    try:
        print BOLD + "Test multiple commands" + ENDC
        child.sendline('echo \"hello world\" | wc -l')
        child.expect(b'1', timeout=2)
        child.sendline('echo hello world|wc -l')
        child.expect(b'1', timeout=2)
        print OKGREEN + "SUCCESS" + ENDC
    except pexpect.TIMEOUT:
        print FAIL + "FAILED" + ENDC
        child.interact()
    except pexpect.EOF:
        print FAIL + "FAILED" + ENDC
        child.interact()
    child.close()

def test_pipe_with_redirection():
    child = pexpect.spawn('./shell')
    try:
        print BOLD + "Test pipe with redirection" + ENDC
        child.sendline('cat 2.4.txt | wc -l > new_file.txt')
        child.expect(b'\s*.*>.*\s*', timeout=2)
        child.sendline('cat new_file.txt')
        child.expect(b'1', timeout=2)
        print OKGREEN + "SUCCESS" + ENDC
    except pexpect.TIMEOUT:
        print FAIL + "FAILED" + ENDC
        child.interact()
    except pexpect.EOF:
        print FAIL + "FAILED" + ENDC
        child.interact()
    child.close()

def test_pipe_with_redirection():
    child = pexpect.spawn('./shell')
    try:
        print BOLD + "Test pipe with redirection" + ENDC
        child.sendline('cat 2.4.txt | wc -l > new_file.txt')
        child.expect(b'\s*.*>.*\s*', timeout=2)
        child.sendline('cat new_file.txt')
        child.expect(b'1', timeout=2)
        print OKGREEN + "SUCCESS" + ENDC
    except pexpect.TIMEOUT:
        print FAIL + "FAILED" + ENDC
        child.interact()
    except pexpect.EOF:
        print FAIL + "FAILED" + ENDC
        child.interact()
    child.close()

def test_pipe_with_background():
    child = pexpect.spawn('./shell')
    try:
        print BOLD + "Test pipe with background" + ENDC
        child.sendline('cat 2.4.txt | wc -l &')
        child.expect(b'1', timeout=2)
        print OKGREEN + "SUCCESS" + ENDC
    except pexpect.TIMEOUT:
        print FAIL + "FAILED" + ENDC
        child.interact()
    except pexpect.EOF:
        print FAIL + "FAILED" + ENDC
        child.interact()
    child.close()

test_pipe_with_spaces()
test_pipe_without_spaces()
test_output_redirection()
test_input_redirection()
test_multiple_commands()
test_pipe_with_redirection()
test_pipe_with_background()
