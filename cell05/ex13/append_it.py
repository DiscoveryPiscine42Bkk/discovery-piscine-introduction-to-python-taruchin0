#!/usr/bin/env python

import sys
import re
parameters = sys.argv

if len(parameters) < 2:
    print("none")
else:
    for i in range(1 , len(parameters)):
        if parameters[i].endswith("ism"):
            continue
        else:
            parameters[i]+="ism"
            print(parameters[i])
            
