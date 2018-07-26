import pexpect
import os

child = pexpect.spawn('./shell')
child.expect('.*>.*', timeout=2)
os.system('kill -INT ' + str(child.pid))

