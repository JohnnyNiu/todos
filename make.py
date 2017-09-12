#!/usr/bin/env python3
import datetime
from pathlib import Path
from subprocess import call


home = str(Path.home())
DIR=home+'/Documents/todos/'

now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d-%a-%H-%M-%S')

file_name = "Todo-%s.md"%now_str
abslute_path = DIR+file_name

title = "### Todo:  (%s)"%now_str

content="\n"
for i in range(0,5):
    content+="- [ ] \n"

content+='\n\n'

content+="### Notes\n"

file=open(abslute_path, 'w+')
file.write(title+content)
file.close()

print("Created: %s"%abslute_path)
call(['open', abslute_path])
