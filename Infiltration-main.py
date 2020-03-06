import requests
import pyperclip
import base64
import keyboard

url='http://challenges.thecatch.cz/781473d072a8de7d454cddd463414034/'

raw=requests.get(url)
txt=raw.text
##print(txt)
patch=txt[txt.find(':')+2:txt.find('Challenge timeout')]
prog=base64.b64decode(patch).decode('utf8')
innum=txt[txt.find(';')+1:]
initnum=base64.b64decode(innum).decode('utf8')
print(initnum)

with open('e:/work/GIT/Catch19_Infiltration/surove.txt',mode='w') as surove:
    surove.write(prog)
    surove.close()

PHXXX=[]
PHYYY=[]
PHZZZ=[]
PLACEHOLDER1=[]

with open('e:/work/GIT/Catch19_Infiltration/surove.txt',mode='r') as surove:
    for line in surove:
        if 'value +=' in line or 'value + =' in line:
            x=line[line.find('=')+3:line.find('=')+5]
            PHXXX.append(x)
        if 'value[' in line:
            y=line[line.find('[')+1:line.find(']')]
            PHYYY.append(y)
        if '] < \"' in line:
            z=line[line.find('<')+3:line.find('<')+4]
            PHZZZ.append(z)
        if '(value)' in line:
            fce='\tvalue = '+line[line.find('=')+2:]
            PLACEHOLDER1.append(fce)


i=0
PH1=''
while i<len(PLACEHOLDER1):
    PH1+=PLACEHOLDER1[i]
    i+=1

pr=''

phx=0

l=''
with open('e:/work/GIT/Catch19_Infiltration/mustr.py',mode='r') as vzor:
    for line in vzor:
        if 'PHXXX' in line:
            l=line.replace('PHXXX',PHXXX[phx])
            phx+=1
            pr+=l
        elif 'PLACEHOLDER2' in line:
            i=0
            while i<len(PHYYY):
                prvni='\n\tif value['+PHYYY[i]+'] < \"'+PHZZZ[i]+'\":\n'
                druha='\t\tvalue += \"'+PHXXX[phx]+'\"\n'
                treti='\telse:\n'
                ctvrta='\t\tvalue += \"'+PHXXX[phx+1]+'\"'
                l=prvni+druha+treti+ctvrta
                pr+=l
                i+=1
                phx+=2
            pr+='\n'
        elif 'PLACEHOLDER1' in line:
            pr+=PH1
        elif 'init_number='in line:
            l=line.replace('init_number=','init_number='+initnum)
            pr+=l
        else:
            pr+=line
vzor.close()
with open('e:/work/GIT/Catch19_Infiltration/progr.py',mode='w') as run:
    run.write(pr)
run.close()

import progr as nove
s=nove.main(initnum)
print(s)

cook=raw.cookies

PAR={'answer':s}
r=requests.get(url,PAR,cookies=cook)

pyperclip.copy(r.text)
print(r.text)           
