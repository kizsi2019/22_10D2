import time
import sys

for i in range(10):
    print("\r🎂 ", end="")
    sys.stdout.flush()
    time.sleep(0.5)
    print("\r 🎂", end="")
    sys.stdout.flush()
    time.sleep(0.5)
