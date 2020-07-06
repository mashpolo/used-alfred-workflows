#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import base64


args = sys.argv
if len(args) <= 1:
	result = u"No result"
else:
	result = base64.b64encode(args[1])
output = {"items": [
    {
        "title": result,
        "arg": result,
        "valid": True
    }
]}


sys.stdout.write(json.dumps(output, sys.stdout, indent=4))
