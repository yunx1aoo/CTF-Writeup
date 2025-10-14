# Riddle Registry

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/dccb5e64-2191-4437-aac7-bb1395ad9004" />

**Tag:** `Forensics` `browser_webshell_solvable`

**Description:** 
> Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered. Find the PDF file here Hidden Confidential Document and uncover the flag within the metadata.

**Attachments:** `confidential.pdf `

**Hints:**

<details>
<summary>Hint 1</summary>

Don't be fooled by the visible text; it’s just a decoy!

</details>

<details>
<summary>Hint 2</summary>
  
Look beyond the surface for hidden clues

</details>

**Author:** Prince Niyonshuti N.

**Solved:** `1.542 users solved`

---

# Solution

because the description says that

> uncover the flag within the metadata.

So to get the flag we only need to check the meta data in the file using `exiftool`

```zsh
 zsh > exiftool confidential.pdf
ExifTool Version Number         : 13.25
File Name                       : confidential.pdf
Directory                       : .
File Size                       : 183 kB
File Modification Date/Time     : 2025:09:30 04:29:21+07:00
File Access Date/Time           : 2025:10:14 10:50:07+07:00
File Inode Change Date/Time     : 2025:10:14 10:50:07+07:00
File Permissions                : -rw-r--r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
Linearized                      : No
Page Count                      : 1
Producer                        : PyPDF2
Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0=
```

Well, in the author section, the flag is still wrapped using base 64 encoding. Let's decode it.

```bash
 zsh > echo 'cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0' | base64 -d
picoCTF{puzzl3d_m3tadata_f0und!_ca76bbb2}%  
```

---

# FLAG: picoCTF{puzzl3d_m3tadata_f0und!_ca76bbb2}
