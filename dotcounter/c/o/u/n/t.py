import sys, os, re

class NotEnoughDotsException(Exception):
    def __init__(self, lineNum):
        super().__init__("Not enough dots on line: %i"%lineNum)

with open(os.path.abspath(sys.argv[0])) as f:
    lines = [line.strip() for line in f]

for i, line in enumerate(lines):
    if line == "":
        continue
    elif re.search("^([^#]*\.){5}", line) is None:
        raise NotEnoughDotsException(i+1)

class C:
    class O:
        class U:
            class N:
                class T:
                    pass
