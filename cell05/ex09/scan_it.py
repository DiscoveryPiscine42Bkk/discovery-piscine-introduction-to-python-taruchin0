#!/usr/bin/env python3

import sys
import re
parameters = sys.argv

if len(parameters)-1 != 2:
    print("none")
else:
    same = re.findall(parameters[1], parameters[2])
    print(len(same))