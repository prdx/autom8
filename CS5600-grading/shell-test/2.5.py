import pexpect
import os
import time

child = pexpect.spawn('./shell')
print "Sleep test case, user should be able to input command after this"
child.sendline('sleep 2 &')
child.sendline('')
child.expect(b'\s*.*>.*\s*', timeout=2)
child.sendline('ps')
child.expect(b'\s*.*>.*\s*', timeout=2)
print child.after

# Wait approx until done
time.sleep(2)

print "Check after the task is done"
print "If it still showing defunc then it is not killed properly"
print "If it is still there without defunct then the process is not done"
child.sendline('ps')
# child.getecho()
# print child.after
child.expect('\s*.*>.*\s*', timeout=2)
print child.after
# child.interact()
child.close()
