[TOC]
# Linux用过指令汇总
## 基础指令
### 权限查看
- 查看文件权限
``
setfacl -x u:user_name xxx.txt
getfacl xxx.txt
``
- 给文件增加x权限
``
chmod -x xxx.txt
``
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