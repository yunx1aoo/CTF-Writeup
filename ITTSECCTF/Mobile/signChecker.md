# Sign Checker

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/d31a749d-0d20-4f14-9c96-0fdc38abe07e" />

---

**Category:** `Mobile`

**Description:**
```
The flag is hidden behind trust. 2^8
```

**Attachments:** `signchecker.apk`

**Difficulty:**

**Points:** `15`

**Author:**

**Date:** 2025-09-24

---

## Solution

we are give a apk file. if i checked using phone there is only have a submit button. if i clicked the button. the response is `invalid sign`

if i checked using linux this is i get it

<img width="499" height="499" alt="image" src="https://github.com/user-attachments/assets/235b2194-f9b0-4d51-bd68-7f119aa30075" />

next i want to disassemble this file using `apktool`. then i check the source code using jadx gui to see what happen in this app

and i found thisss. 

```kotlin
    public static final Unit SubmitScreen$lambda$6$lambda$5$lambda$4(final MutableState $responseText$delegate) {
        makeRequest("https://mit.ittsec.net/?flag=0", new Function1() { // from class: com.example.ittsecmobile2.MainActivityKt$$ExternalSyntheticLambda2
            @Override // kotlin.jvm.functions.Function1
            public final Object invoke(Object obj) {
                return MainActivityKt.SubmitScreen$lambda$6$lambda$5$lambda$4$lambda$3($responseText$delegate, (String) obj);
            }
        });
        return Unit.INSTANCE;
    }
```

if we check the url 

<img width="687" height="164" alt="image" src="https://github.com/user-attachments/assets/af41e05b-faa5-4584-b60d-c4cc4cec0da6" />

the response is same when i clicked submit button in app. i think this app get response from that web

after that i checked the asm code. and found a function. i think this function do xor with something but i must check it first

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/08d46833-fbce-4232-a72e-aa770f269f14" />

after exploring the code i found the key of xor. this function use 0x55 to encrypt the data

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/c01ba85d-5c31-44b9-abbf-498ce59d883f" />

after get the key. i disas again and search for the data. and i found 2 data in this app. they are a little endian data. the data like this:

data 1

```asm
   24d0b:       e8 c0 2f 03 00          call   57cd0 <_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180000ILi0EEEPKc@plt>
   24d10:       8b 9d 70 ff ff ff       mov    -0x90(%ebp),%ebx
   24d16:       66 c7 45 f4 32 68       movw   $0x6832,-0xc(%ebp)
   24d1c:       c7 45 f0 6a 33 39 34    movl   $0x3439336a,-0x10(%ebp)
   24d23:       89 e0                   mov    %esp,%eax
   24d25:       8d 4d f0                lea    -0x10(%ebp),%ecx
```

data 2

```asm
  24d3e:       e8 2d 2f 03 00          call   57c70 <_Z9xorDecodePKhjh@plt>
   24d43:       83 ec 04                sub    $0x4,%esp
   24d46:       e9 00 00 00 00          jmp    24d4b <Java_com_example_ittsecmobile2_MainActivity_getAutoUrl@@Base+0x7b>
   24d4b:       8b 9d 70 ff ff ff       mov    -0x90(%ebp),%ebx
   24d51:       66 c7 45 ec 3b 68       movw   $0x683b,-0x14(%ebp)
   24d57:       c7 45 e8 73 26 3c 32    movl   $0x323c2673,-0x18(%ebp)
```

after get the data. next i want to decrypt the data use key 0x55.

```python
 zsh > python
Python 3.13.7 (main, Aug 20 2025, 22:17:40) [GCC 14.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import xor
>>> data1 = [0x6a, 0x33, 0x39, 0x34, 0x32, 0x68]
>>> data2 = [0x73, 0x26, 0x3c, 0x32, 0x3b, 0x68]
>>> key = 0x55
>>> print(data1)
[106, 51, 57, 52, 50, 104]
>>> print(xor(data1, key))
b'?flag='
>>> print(xor(data2,key))
b'&sign='
```

i think the parameter is use for the web so i add the parameter on the web

<img width="500" height="100" alt="image" src="https://github.com/user-attachments/assets/6b72985f-a25a-4d47-92fe-0a9ed837de4b" />

but still not get the flag. if checked the description. it said `The flag is hidden behind trust. 2^8`. `2^8` is `256`

i think thats is a sha256. so i change the parameter `flag=0` to `flag=1`. and fill sign parameter with sha 256 like this

<img width="300" height="102" alt="image" src="https://github.com/user-attachments/assets/f0927bb7-4489-47a7-9ba7-2689cebdb266" />

so we can fill the result to `sign=6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b`

okay now lets get the flag

<img width="500" height="122" alt="image" src="https://github.com/user-attachments/assets/9159b821-acb0-48e5-8188-c9b9b907d335" />


## Flag

```
ITTSec{ssl_piNn1ng_is_only_illusi0n}
```

## Tools & Techniques

`ssl`
`sha256`
`apktool`
`jadx-gui`

---
*Writeup by yunx1ao - 2025-09-23*
