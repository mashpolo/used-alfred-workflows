import json
import subprocess
from ast import literal_eval


user_info = subprocess.getoutput('echo `pbpaste`')
try:
    base_dict = literal_eval(user_info.replace('true', 'True'))
    result = json.dumps(base_dict, indent=4)
    with open("/tmp/tmpabc.txt", mode='w', encoding='utf-8') as f:
        f.write(result)
    subprocess.getoutput("open /tmp/tmpabc.txt")
except Exception as ex:
    print(ex)
