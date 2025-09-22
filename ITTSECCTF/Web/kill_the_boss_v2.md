# kill the boss v2

<img width="300" height="300" alt="屏幕截图 2025-09-21 212929" src="https://github.com/user-attachments/assets/f5823f02-0ee5-4f79-a82f-500f025726f7" />

---

**Category:** `Web`

**Description:**
```
https://web3.ittsec.net/
```

**Difficulty:**

**Points:** `10`

**Author:**

**Date:** 2025-09-23

---

## Solution

<img width="500" height="500" alt="屏幕截图 2025-09-21 213309" src="https://github.com/user-attachments/assets/79f1d93b-4fd4-4e30-a036-a8c64844018f" />

we are given another cool ui. where we have a fight between the minions and the dragon king part two

<img width="500" height="500" alt="屏幕截图 2025-09-21 213325" src="https://github.com/user-attachments/assets/20fe5bf5-12a2-4a30-a435-5dbb55a45d20" />

When I click attack here, there's something different. This time the parameters are hidden. If I check using burp suite

<img width="281" height="300" alt="屏幕截图 2025-09-21 213603" src="https://github.com/user-attachments/assets/12af15b6-df4e-4ae9-a92b-47d6f45480c7" />

It turns out that a request was sent, but it was sent using base 64 encoding. If we decode the contents, it will look like this.

<img width="500" height="400" alt="屏幕截图 2025-09-21 213636" src="https://github.com/user-attachments/assets/0ea53175-d944-40da-904f-bbb321f85a64" />

same as before, the only difference is that this time the data is encoded using base64

we just need to resend the request with the same encoding and change the value to, for example, here I changed it to 100

<img width="300" height="400" alt="屏幕截图 2025-09-21 213702" src="https://github.com/user-attachments/assets/02dda94c-b5fa-4bde-a1e8-cd9fcca70c96" />

Now we replace the previous value with the new value that we have encoded

<img width="282" height="195" alt="屏幕截图 2025-09-21 213712" src="https://github.com/user-attachments/assets/78ee0725-cf0d-4b02-ab97-e9899798b27a" />

click send on burp suite

<img width="665" height="277" alt="屏幕截图 2025-09-21 213728" src="https://github.com/user-attachments/assets/4cf1944b-99a8-4608-92b3-55c75560f5e8" />


## Flag

```
ITTSec(p4r4m3t3r_t4mp3ring_v14_p0st_b4s364_ftw)
```

## Tools & Techniques

`burpsuite`
`web parameter tampering`
`base64 encoding`

---
*Writeup by spl1t4t3rminal - 2025-09-23*
