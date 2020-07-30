import os, sys

os.system('/home/ais3/AIS3-2020/final_project/objconv/objconv '
         +'-fnasm '+sys.argv[1]+' tmp123123.s')
f = [i.split(';')[0] for i in open('tmp123123.s','r').read().split('\n')]

f = '\n'.join([i for i in f if i!=''])
f = '\n'.join([i for i in f.split('\n') if 'ALIGN' not in i])
f = '\n'.join([i for i in f.split('\n') if 'extern' not in i])
f = '\n'.join([i for i in f.split('\n') if 'default' not in i])
f = '\n'.join([i for i in f.split('\n') if 'global' not in i])
f = ['\n'.join(i.split('\n')[1:]) for i in f.split('SECTION') if 'noexecute' not in i]
output = '\n'.join(f).replace(': ',':\n       ').replace('\n\n','\n')
print(output)
with open(sys.argv[1].replace('./','').replace('.out','')+'.s','w') as f:
    f.write(output)
os.system('rm tmp123123.s')
