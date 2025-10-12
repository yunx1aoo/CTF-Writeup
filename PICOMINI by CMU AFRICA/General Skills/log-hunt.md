# Log Hunt

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/7d374e92-a0c6-485b-945d-d01e461f48c0" />

**Tag:** `General Skills` `browser_webshell_solvable`

**Description:** 
> Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag? Download the logs and figure out the full flag from the fragments.

**Attachments:** `server.log`

**Hints:**

<details>
<summary>Hint 1</summary>

You can use `grep` to filter only matching lines from the log.

</details>

<details>
<summary>Hint 2</summary>
  
Some lines are duplicates; ignore extra occurrences.

</details>

**Author:** Yahaya Meddy

**Solved:** `1.778 users solved`

---

#  Solution

I use Visual Studio Code to understand the entire contents of the code, which can be seen in the image below.

<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/502969c5-e35e-4665-9bec-f8e5f3cf3a3a" />

from the picture we have found 2 flag parts. `picoCTF{us3` and `y0urlinux_`. But if we make sense of it, there are still some missing pieces of the flag. I continued searching for the missing pieces of the flag.
there he uses a help word in front of it, namely FLAGPART. Next I used a combination of strings grep to try to catch all affixes that said FLAGPART

```zsh
 zsh > strings server.log | grep FLAGPART
[1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
[1990-08-09 10:02:55] INFO FLAGPART: y0urlinux_
[1990-08-09 10:05:54] INFO FLAGPART: sk1lls_
[1990-08-09 10:05:55] INFO FLAGPART: sk1lls_
[1990-08-09 10:10:54] INFO FLAGPART: cedfa5fb}
[1990-08-09 10:10:58] INFO FLAGPART: cedfa5fb}
[1990-08-09 10:11:06] INFO FLAGPART: cedfa5fb}
[1990-08-09 11:04:27] INFO FLAGPART: picoCTF{us3_
[1990-08-09 11:04:29] INFO FLAGPART: picoCTF{us3_
[1990-08-09 11:04:37] INFO FLAGPART: picoCTF{us3_
[1990-08-09 11:09:16] INFO FLAGPART: y0urlinux_
[1990-08-09 11:09:19] INFO FLAGPART: y0urlinux_
[1990-08-09 11:12:40] INFO FLAGPART: sk1lls_
[1990-08-09 11:12:45] INFO FLAGPART: sk1lls_
[1990-08-09 11:16:58] INFO FLAGPART: cedfa5fb}
[1990-08-09 11:16:59] INFO FLAGPART: cedfa5fb}
[1990-08-09 11:17:00] INFO FLAGPART: cedfa5fb}
[1990-08-09 12:19:23] INFO FLAGPART: picoCTF{us3_
[1990-08-09 12:19:29] INFO FLAGPART: picoCTF{us3_
[1990-08-09 12:19:32] INFO FLAGPART: picoCTF{us3_
[1990-08-09 12:23:43] INFO FLAGPART: y0urlinux_
[1990-08-09 12:23:45] INFO FLAGPART: y0urlinux_
[1990-08-09 12:23:53] INFO FLAGPART: y0urlinux_
[1990-08-09 12:25:32] INFO FLAGPART: sk1lls_
[1990-08-09 12:28:45] INFO FLAGPART: cedfa5fb}
[1990-08-09 12:28:49] INFO FLAGPART: cedfa5fb}
[1990-08-09 12:28:52] INFO FLAGPART: cedfa5fb}
```

and yes we got it all lol. now we just need to string the flag pieces together

---
# FLAG: picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}
