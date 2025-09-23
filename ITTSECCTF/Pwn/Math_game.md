# Math game

<img width="300" height="300" alt="屏幕截图 2025-09-21 213001" src="https://github.com/user-attachments/assets/deaeef67-5906-4e07-a882-2baacdd88355" />

---

**Category:** `Pwn`

**Description:**
```
Bisakah kamu mengalahkannya?
```

**Attachments:** `math_game`

**Difficulty:**

**Points:** `12`

**Author:**

**Date:** 2025-09-23

---

## Solution

in this challenge an executable file is given which. Actually, I'm confused about the context of this challenge, whether it's a `pwn` or `reverse engineering`. The method I'm using here is the `reverse engineering` method.

First I checked the file type to see if this was a Linux or Windows file.and check if we can get the flag straight away and I only got a fake flag

<img width="500" height="164" alt="image" src="https://github.com/user-attachments/assets/e66acbd6-257b-4b00-a203-52988b8c7c09" />

Next I give permission to the file to see how this program runs and from there we can know which steps we will take

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/5c819687-36a7-49db-ab0d-7a35624888ca" />

I think it's too crazy that he asked us to answer the questions quickly. If we don't answer them, we will immediately lose.

Next, the account uses `GDB` to check what functions are in this code. 

```bash
gef➤  info functions
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x00000000000010e0  __cxa_finalize@plt
0x00000000000010f0  __stack_chk_fail@plt
0x0000000000001100  alarm@plt
0x0000000000001110  srand@plt
0x0000000000001120  __sysv_signal@plt
0x0000000000001130  time@plt
0x0000000000001140  fflush@plt
0x0000000000001150  __printf_chk@plt
0x0000000000001160  __isoc99_scanf@plt
0x0000000000001170  sleep@plt
0x0000000000001180  getc@plt
0x0000000000001190  rand@plt
0x00000000000011a0  main
0x0000000000001440  _start
0x0000000000001470  deregister_tm_clones
0x00000000000014a0  register_tm_clones
0x00000000000014e0  __do_global_dtors_aux
0x0000000000001520  frame_dummy
0x0000000000001530  timer_handler
0x0000000000001540  deobfuscate_flag
0x0000000000001580  generate_hard_math
0x00000000000017d0  print_banner
0x0000000000001870  _fini
```

what's interesting is that there is a function that deobfuscates the flag there. Next I did a disas on the function to get a glimpse of how it works.

```bash
gef➤  disas deobfuscate_flag
Dump of assembler code for function deobfuscate_flag:
   0x0000000000001540 <+0>:     endbr64
   0x0000000000001544 <+4>:     mov    edx,0xb
   0x0000000000001549 <+9>:     xor    eax,eax
   0x000000000000154b <+11>:    lea    rcx,[rip+0x112e]        # 0x2680 <obfuscated_flag>
   0x0000000000001552 <+18>:    jmp    0x155c <deobfuscate_flag+28>
   0x0000000000001554 <+20>:    nop    DWORD PTR [rax+0x0]
   0x0000000000001558 <+24>:    movzx  edx,BYTE PTR [rcx+rax*1]
   0x000000000000155c <+28>:    xor    edx,0x42
   0x000000000000155f <+31>:    mov    BYTE PTR [rdi+rax*1],dl
   0x0000000000001562 <+34>:    add    rax,0x1
   0x0000000000001566 <+38>:    cmp    rax,0x2d
   0x000000000000156a <+42>:    jne    0x1558 <deobfuscate_flag+24>
   0x000000000000156c <+44>:    mov    BYTE PTR [rdi+0x2d],0x0
   0x0000000000001570 <+48>:    ret
End of assembler dump.
```

it can be seen that the function performs an xor on the flag. Next I did a check in Ghidra and looked for the `deobfucate_flag` function.

And after decompilation, here's the contents of the deobfuscate_flag function. It appears to be performing an xor with the key 0x42.

```cpp

void deobfuscate_flag(long param_1)

{
  long lVar1;
  byte bVar2;
  
  bVar2 = 0xb;
  lVar1 = 0;
  while( true ) {
    *(byte *)(param_1 + lVar1) = bVar2 ^ 0x42;
    if (lVar1 + 1 == 0x2d) break;
    bVar2 = obfuscated_flag[lVar1 + 1];
    lVar1 = lVar1 + 1;
  }
  *(undefined1 *)(param_1 + 0x2d) = 0;
  return;
}


```

there you can see obfuscated_flag which when clicked takes us to the xored flag fragment

```asm
           00102680 0b              undefined10Bh                     [0]                             
                                                                                                                 
           00102681 16              undefined116h                     [1]                            
           00102682 16              undefined116h                     [2]
           00102683 11              undefined111h                     [3]
           00102684 27              undefined127h                     [4]
           00102685 21              undefined121h                     [5]
           00102686 39              undefined139h                     [6]
           00102687 2f              undefined12Fh                     [7]
           00102688 76              undefined176h                     [8]
           00102689 36              undefined136h                     [9]
           0010268a 2a              undefined12Ah                     [10]
           0010268b 1d              undefined11Dh                     [11]
           0010268c 0f              undefined10Fh                     [12]
           0010268d 23              undefined123h                     [13]
           0010268e 31              undefined131h                     [14]
           0010268f 36              undefined136h                     [15]
           00102690 27              undefined127h                     [16]
           00102691 30              undefined130h                     [17]
           00102692 1d              undefined11Dh                     [18]
           00102693 70              undefined170h                     [19]
           00102694 72              undefined172h                     [20]
           00102695 70              undefined170h                     [21]
           00102696 77              undefined177h                     [22]
           00102697 1d              undefined11Dh                     [23]
           00102698 2b              undefined12Bh                     [24]
           00102699 2f              undefined12Fh                     [25]
           0010269a 32              undefined132h                     [26]
           0010269b 2d              undefined12Dh                     [27]
           0010269c 31              undefined131h                     [28]
           0010269d 31              undefined131h                     [29]
           0010269e 2b              undefined12Bh                     [30]
           0010269f 20              undefined120h                     [31]
           001026a0 2e              undefined12Eh                     [32]
           001026a1 71              undefined171h                     [33]
           001026a2 1d              undefined11Dh                     [34]
           001026a3 21              undefined121h                     [35]
           001026a4 2a              undefined12Ah                     [36]
           001026a5 23              undefined123h                     [37]
           001026a6 2e              undefined12Eh                     [38]
           001026a7 2e              undefined12Eh                     [39]
           001026a8 27              undefined127h                     [40]
           001026a9 2c              undefined12Ch                     [41]
           001026aa 25              undefined125h                     [42]
           001026ab 27              undefined127h                     [43]
           001026ac 3f              undefined13Fh                     [44]
           001026ad 42              undefined142h                     [45]

```

Since we've already got the flag pieces, we just need to reverse the logic by doing a re-XOR with key 0x42.

```python
zsh > python
>>> from pwn import xor
>>> flag = [0x0b, 0x16, 0x16, 0x11, 0x27, 0x21, 0x39, 0x2f, 0x76, 0x36, 0x2a, 0x1d, 0x0f, 0x23, 0x31, 0x36, 0x27, 0x30, 0x1d, 0x70, 0x72, 0x70, 0x77, 0x1d,\ 0x2b,0x2f, 0x32, 0x2d, 0x31, 0x31, 0x2b, 0x20, 0x2e, 0x71, 0x1d, 0x21, 0x2a, 0x23, 0x2e, 0x2e, 0x27, 0x2c, 0x25, 0x27, 0x3f, 0x42]
>>> key = 0x42
>>> print(xor(flag, key))
b'ITTSec{m4th_Master_2025_impossibl3_challenge}\x00'
```

## Flag

```
ITTSec{m4th_Master_2025_impossibl3_challenge}
```

## Tools & Techniques

`gdb` `ghidra` `pwn` `python` 

---
*Writeup by yunx1ao - 2025-09-23*
