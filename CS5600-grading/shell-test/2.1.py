import pexpect

child = pexpect.spawn('./shell')
child.sendline('help')
child.expect(b'\s*.*>.*\s*', timeout=2)
print child.after

child.interact()
