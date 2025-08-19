# Admin Panel - 300 Points
**Description:** `I designed the most secure admin panel ever.`

**Attachments:** `Admin_panel`


---

We are given an `Admin_panel` file. First, let's check the file type using the `file` command.

<img width="1893" height="76" alt="屏幕截图 2025-08-19 133928" src="https://github.com/user-attachments/assets/abc82471-ae8b-480c-8e56-5e5cbb195cb4" />

Next, let's check the security with `checksec`, the most important thing is whether the pie is disabled or not.

<img width="1912" height="83" alt="屏幕截图 2025-08-19 142741" src="https://github.com/user-attachments/assets/d1dbd7ac-a620-423c-a4fc-4e46b7b3febb" />

Then, let's run this program by giving it permission using `chmod` and run `./Admin_panel`

<img width="394" height="138" alt="屏幕截图 2025-08-19 135429" src="https://github.com/user-attachments/assets/8e2865e0-2888-4d0b-a5c4-a1bec805147d" />

So this program runs by asking if we are admin, whatever I do, this program never returns I am admin, which means we can assume that to get the `flag` we have to be admin in this program.

Let's try to find interesting words like `flag`, `admin`, `CRHC (format flag)`, `key` and also `pass` using `strings` and `grep`.

<img width="764" height="335" alt="屏幕截图 2025-08-19 140051" src="https://github.com/user-attachments/assets/d19590c6-5f39-4631-84fd-2691fc8dd062" />

Well, there are several words that were taken, and they most likely came from `.text` or `.rodata`.

What is `.rodata` and `.text` can be seen here

**https://medium.com/@johnehk86/66-what-are-memory-and-sections-text-data-bss-rodata-etc-e134bd5b9ccd**

So, to find out more details, let's try to find `.rodata` and also `.text` using `readelf`, this is a fairly powerful command for elf type files.

<img width="833" height="73" alt="屏幕截图 2025-08-19 143306" src="https://github.com/user-attachments/assets/7e44865e-4964-4487-b568-731eb15591b5" />

I was a bit confused at this point, so I asked my bro `ChatGPT` hhe. He explained the `base file` and the `virtual address`, which determines the `instruction address`. He also gave me the formula for finding the `instruction address`.

this is the formula he gave

> file_offset=offset_base+(VA−VA_base)

> VA=file_offset−file_offsetbase​+VAbase​

but for now it's not very useful because we will use it later, let's continue whahahh

Now let's first find out where this program starts by using `objdump` which checks the `.rodata` data.

<img width="747" height="266" alt="屏幕截图 2025-08-19 145629" src="https://github.com/user-attachments/assets/d8af5dbb-80e2-407e-965f-c39eb34a356f" />

From the output, we know that the are you admin is at offset 49e030. Let's check the code using objdump and grep the offset.

<img width="1054" height="51" alt="屏幕截图 2025-08-19 150203" src="https://github.com/user-attachments/assets/e189f26b-9bbf-49b4-bab7-7fcadbaddcfa" />



Okay, interesting. Honestly, when I got that output, I immediately did some research on lea. And yeah, there's nothing interesting, so let's just skip this, hehe. But pay attention to that line, it's on line `724`. Let's take some code snippets starting from 724 to I don't know v:. The point is, we get to the important part of the code. We'll check it using `objdump` and `sed/stream editor`.

To be honest, I'm not an assembly expert, but I understand a little about how assembly works and how the code blocks work. Here's a brief explanation.

```bash
objdump -d Admin_Panel | sed -n '721,770p' | nl -ba
401a79: 00 00
401a7b: 48 89 45 f8      mov %rax,-0x8(%rbp)
401a7f: 31 c0             xor %eax,%eax
401a81: 48 8d 05 a8 c5 09 00   lea 0x9c5a8(%rip),%rax
401a88: 48 89 c7          mov %rax,%rdi
401a8b: e8 10 c5 00 00    call 0x40dfa0
401a90: 48 8d 45 70       lea -0x70(%rbp),%rax
401a94: 48 89 c6          mov %rax,%rsi
401a97: 48 8d 05 a1 c5 09 00   lea 0x9c5a1(%rip),%rax   # 0x49e03f
401a9e: 48 89 c7          mov %rax,%rdi
401aa1: b8 00 00 00 00    mov $0x0,%eax
401aa6: e8 a5 34 00 00    call 0x404f50
401aab: c7 45 8c 01 00 00 00    movl $0x1,-0x74(%rbp)   < This is where the variable declaration begins.
401ab2: 83 7d 8c 01             cmpl $0x1,-0x74(%rbp)   < then the program performs a comparison with the number
401ab6: 75 16                   jne 0x401ace           < This is the part that compares the variable with the number 1. Because the variable declaration was 1, this will return ZF = 1. And that will affect the jne below it.
401ab8: 48 8d 05 89 c5 09 00    lea 0x9c589(%rip),%rax  # 0x49e048 < this is probably the 'aww not admin' part
401abf: 48 89 c7                mov %rax,%rdi          < this is a function that says we are not admins
401ac2: e8 d9 c4 00 00          call 0x40dfa0
401ac7: b8 00 00 00 00          mov $0x0,%eax
401acc: eb 0f                   jmp 0x401add
401ace: b8 00 00 00 00          mov $0x0,%eax
401ad3: e8 8d fe ff ff          call 0x401965        < Here the function states that we are real admins


```
---
Patched
---

OK, it's easy, all we have to do is patch this block.
```
    13    401aab:       c7 45 8c 01 00 00 00    movl   $0x1,-0x74(%rbp)
```

we have to change the variable declaration to 0 so that when compared it produces ZF = 0

Let's use the formula that my friend gave us earlier to find the correct instruction address when the program is run

> file_offset = (0x401aab - 0x4011c0) + 0x11c0 = 0x1aab

Okay, because I don't know but I pretend to know. Actually, I experienced a patch failure. Then I asked my friend. And it turns out that besides having to find the base offset for the instruction address, it's also necessary to find the instruction that works directly on the instruction. I don't really understand it. And this is the formula given.

> file_off_instr = (0x401aab - 0x4011c0) + 0x11c0 = 0x1aab

> file_off_imm   = file_off_instr + 3 = 0x1aae

so we get the offset we need to hit which is 0x1aae

Before we start, I will backup first, haha. I'm afraid of failure, so we have to backup the file first, because I'm too lazy to download it again.

Use this command:
```
cp -n Admin_Panel Admin_Panel.bak
```

we have to patch `01 00 00 00` with `00 00 00 00` which will return zf = 0 and will jump directly to the flag

time patching wahahhahahah

try this command:
```bash
printf '\x00\x00\x00\x00' | dd of=Admin_panel bs=1 seek=$((0x1aae)) conv=notrunc
```

okay lets check our patch is verified or not use this:
```bash
hexdump -Cv Admin_panel | grep -n "c7 45 8c 00 00 00 00" 
```

if successful it will be like this
```bash
hexdump -Cv Admin_panel | grep -n "c7 45 8c 00 00 00 00"
15204:0003b630  00 00 48 8b 81 28 02 00  00 c7 45 8c 00 00 00 00  |..H..(....E.....|
```
Okay, if you feel confident, hahaha. Let's just try it.

```bash
❯ ./Admin_panel
Are you admin?
no i'm not admin, now you can trust me
CRHC{It's_noT_poss1bl3!!!}
```

<img width="423" height="97" alt="image" src="https://github.com/user-attachments/assets/8b3541c4-e256-42db-8284-3b51a08718e2" />



i'm says I'm not an admin. How come I got the flag lol. This is a fun reverse challenge in my opinion haha. We don't need ghidra because we only need to patch 1 block of code and boommmm hahah

I also thank my bro who was willing to help me when I was stuck.

Thank you for reading my writeup. I'm here to learn with all of you. **Happy CTF**


