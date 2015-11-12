#!/usr/bin/env python

import json
import random
import time
import random

#
# Open are parse the param.json file
#
with open("param.json") as f:
    parameters = json.load(f)

# Extract the plugin configuration
source = parameters["source"]
poll_interval = parameters["poll_interval"]

# Metric identifier
metric = 'PYTHON_HELLO_WORLD'

while True: 
    timestamp = int(time.time())
    value = random.randrange(0, 99)
    print("{0}, {1}, {2}, {3}".format(metric, source, value, timestamp))
    time.sleep(poll_interval)
