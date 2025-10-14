# Corrupted File

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/9ff6c7c7-04c5-4776-b1aa-8e31a6676fba" />

**Tag:** `Forensic` `browser_webshell_solvable`

**Description:** 
> This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life? Download the file here.

**Attachments:** `file`

**Hints:**

<details>
<summary>Hint 1</summary>

Try checking the file’s header.

</details>

<details>
<summary>Hint 2</summary>
  
JPEG

</details>


<details>
<summary>Hint 3</summary>
  
Tools like xxd or hexdump can help you inspect and edit file bytes.

</details>

**Author:** Yahaya Meddy

**Solved:** `1.144 users solved`

---

# Solution

We are given corrupted data. If we check the file type of the attachments, it will look like this.

```zsh
 zsh > file file
file: data
```

So let's try using xxd to check the bytes of this code.

```asm
 zsh > xxd file | head -5
00000000: 5c78 ffe0 0010 4a46 4946 0001 0100 0001  \x....JFIF......
00000010: 0001 0000 ffdb 0043 0008 0606 0706 0508  .......C........
00000020: 0707 0709 0908 0a0c 140d 0c0b 0b0c 1912  ................
00000030: 130f 141d 1a1f 1e1d 1a1c 1c20 242e 2720  ........... $.'
00000040: 222c 231c 1c28 3729 2c30 3134 3434 1f27  ",#..(7),01444.'
```

We can see there is a JFIF which indicates that this file is a JPEG. This is exactly the same as the hint given. and it appears that the prefix bit/signature of the file header has an error, this is what causes the file to be corrupted. JPEG should be built with the prefix byte `FF D8 FF EE`

We can find out all the list of signature header files on wikipedia. Here is the link.

```
https://en.wikipedia.org/wiki/List_of_file_signatures
```

Next I will fix the header using a hex editor

<img width="872" height="86" alt="image" src="https://github.com/user-attachments/assets/58eeecb4-ffb6-4b57-a801-72d3e3368701" />

let's replace those wrong bytes into this

<img width="288" height="89" alt="image" src="https://github.com/user-attachments/assets/57f3af41-a39d-414f-8b64-0f014d1f3554" />

<img width="875" height="175" alt="image" src="https://github.com/user-attachments/assets/42f37695-ad40-46d2-8e70-df02f20e6826" />

then we save as using the .jpeg extension. then open the image and get the flag

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/312052c1-8a88-476b-9d9b-516c9a2c04c0" />

# FLAG: picoCTF{r3st0r1ng_th3_by73s_efd8c6c0}
