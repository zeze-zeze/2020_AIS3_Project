#!/usr/bin/python
import os, sys

if len(sys.argv)==1:
    print('''Usage: obj2asm.py infile [outfile]''')


os.system('/home/ais3/AIS3-2020/final_project/objconv/objconv '
         +'-fnasm '+sys.argv[1]+' tmp123123.s')
f = '\n'.join([i.split(';')[0] for i in open('tmp123123.s','r').read().split('\n')])
f = '\n'.join([i.split(';')[0] for i in open('tmp123123.s','r').read().split('\r')])
f = '\n'.join([i for i in f.split('\n') if i!=''])
f = '\n'.join([i for i in f.split('\n') if 'ALIGN' not in i])
f = '\n'.join([i for i in f.split('\n') if 'extern' not in i])
f = '\n'.join([i for i in f.split('\n') if 'default' not in i])
f = '\n'.join([i for i in f.split('\n') if 'global' not in i])
f = f.replace('?_0','.L')
f = f.replace('?_1','.L1')
f = f.replace('.L0','.L')
f = f.replace('.L0','.L')
f = f.replace('.L0','.L')
f = f.replace('.L0','.L')
f = '\n'.join(['\n'.join(i.split('\n')[1:]) for i in f.split('SECTION') if 'noexecute' not in i and 'plt' not in i])
f = 'fs:'.join([i.replace(':',':\n       ') for i in f.split('fs:')])
output = '\n'.join([i for i in f.split('\n') if i.strip()!=''])

if len(sys.argv)>=3:
    with open(sys.argv[2],'w') as f:
        f.write(output)

else:
    with open(sys.argv[1].replace('./','').replace('.out','')+'.s','w') as f:
        f.write(output)


os.system('rm tmp123123.s')
