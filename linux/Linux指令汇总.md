[TOC]
# Linux用过指令汇总
## 基础指令
### 权限
- 查看文件权限
``
setfacl -x u:user_name xxx.txt
getfacl xxx.txt
``
- 给文件增加x权限
``
chmod -x xxx.txt
``
- 给命令设置长期root管理
  将nmap的可执行文件设置为SUID（设置UID）位，以使其拥有root权限。使用以下命令进行设置：
- ````bash
  sudo chmod u+s /usr/bin/nmap
  ````
## 常见工具
### gcc
- 将 getbuf.s 文件汇编成二进制可执行文件 getbuf
``
gcc -c -o getbuf.o getbuf.s
gcc -o getbuf getbuf.o
``
## 调试工具
### gdb调试公式
- **运用前提**：进入到gdb(pwngdb)环境,调试ctarget
  ``
    gdb ctarget
  ``
-  反汇编出函数getbuf
  ``
  disass getbuf
  ``
- 在某个函数处设断点
````
  break getbuf（函数）
  break *0x401958(特定地址)
  开始执行或重新执行：
  run
  如果遇到拦截：
  run -q

  单步调试：
  s(step) -进入函数
  n(next) -跳出函数的下一步

  此时可查特定或所有寄存器：
  info ingisters rsp
````



## 工具反汇编
### objdump 反汇编工具
- 将ctarget程序反汇编并存入txt中
``
objdump -d ctarget >ctarget.txt 
``
- 在ctarget程序中找到touch1函数
``
objdump -t ctarget | grep touch1
``
找到的格式：
``
000000000040195d(地址) g（输出符号）     F（储存的为可执行代码） .text（代码位于代码段）	000000000000002c（存储的代码段大小即代码的字节数）              touch1
``
> objdump输出符号：
> g 表示该符号是全局的，即该符号在整个程序中都是可见的。 l（局部符号）、d（已定义的数据）、u（未定义的符号）
## 扫描工具
### nmap
`nmap -sS -sV -T5 -A 192.168.4.202`
该命令是用于扫描目标IP地址（这里是192.168.4.202）并获取其开放的端口和运行的服务信息。
*   `-sS`：使用TCP SYN扫描，也称为半开放扫描。它发送一个SYN包到目标主机的每个扫描端口，如果端口处于打开状态，它将返回一个SYN/ACK响应。
*   `-sV`：启用版本检测，即获取目标主机上运行的每个开放服务的版本信息。
*   `-T5`：设置扫描速度。值越高，扫描速度越快，但也会增加被探测主机发现的风险。在这种情况下，扫描速度设置为5（最高速度）。
*   `-A`：启用操作系统检测、版本检测、脚本扫描和跟踪路由信息等选项。