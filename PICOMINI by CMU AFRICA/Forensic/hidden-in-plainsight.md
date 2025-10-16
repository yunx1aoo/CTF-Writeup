# Hidden in Plainsight

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/4c5bd21e-cf83-4e31-bcde-2e10b31a4113" />

**Tag:** `Forensics` `browser_webshell_solvable`

**Description:** 
>You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag. Download the jpg image here.

**Attachments:** `img.jpg`

**Hints:**

<details>
<summary>Hint 1</summary>

Download the jpg image and read its metadata

</details>

**Author:** Yahaya Meddy

**Solved:** `1.205 users solved`

---

# Solution

I was given an image file with a jpg extension. I then checked using the `file` to verify that it was indeed a jpg. But I accidentally found something.

```bash
 zsh > file img.jpg
img.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9", baseline, precision 8, 640x640, components 3
```

you can see there is a section comment that contains base64 encoding. let's try to decode it. 

```bash
 zsh > echo 'c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9' | base64 -d
steghide:cEF6endvcmQ=
```

Okay, there's an important clue next pointing to steghide and there's another base 64 encoding. Let's decode it again.

```zsh
 zsh > echo 'cEF6endvcmQ' | base64 -d
pAzzword% 
```

It seems that there is a password. We can assume that we have to extract an embedded data using the steghide and password.

```zsh
 zsh > steghide extract -sf img.jpg -p "pAzzword"
wrote extracted data to "flag.txt".
```

and that's right let's read the file

```bash
 zsh > tail flag.txt
picoCTF{h1dd3n_1n_1m4g3_e7f5b969}
```

---

# FLAG: picoCTF{h1dd3n_1n_1m4g3_e7f5b969}
