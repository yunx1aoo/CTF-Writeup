# unsecured web

<img width="300" height="300" alt="屏幕截图 2025-09-21 212939" src="https://github.com/user-attachments/assets/e7392b46-7fce-4190-a21b-cf5fe4593242" />

---

**Category:** `Web`

**Description:**

**Attachments:** `https://web5.ittsec.net/`

**Difficulty:**

**Points:** `12`

**Author:**

**Date:** 2025-09-23

---

## Solution

<img width="500" height="500" alt="屏幕截图 2025-09-23 143758" src="https://github.com/user-attachments/assets/8e3b8b72-5613-44eb-9493-d22448824662" />

We are given a company landing page. There are three features: home, about, and contact. I tried to check the source code

<img width="500" height="108" alt="屏幕截图 2025-09-23 154115" src="https://github.com/user-attachments/assets/eb1f6a24-4003-457d-902f-f375dc7b341e" />

and I found something. most likely this is an LFI exploit. Next I clicked on one of the 3 navbar features

<img width="500" height="200" alt="屏幕截图 2025-09-23 143808" src="https://github.com/user-attachments/assets/af52741c-1438-4752-af64-08ab84e8a39f" />

to prove whether this is LFI or not i tried to do a general pattern in LFI

<img width="500" height="500" alt="屏幕截图 2025-09-23 154000" src="https://github.com/user-attachments/assets/4c478593-ce9c-4001-8b73-5ca75b02e143" />

BINGOO. It turns out this is LFI. After I realized it, I tried to find where the flag was but couldn't find it, but when I tried `flag.php`

<img width="500" height="500" alt="屏幕截图 2025-09-23 143838" src="https://github.com/user-attachments/assets/e7537761-aabf-49be-8415-a257d8b34946" />

The page doesn't display any errors, which if it were wrong I would have received a file not found warning, but it doesn't. It's white

I did some research and found one of the filter techniques here -> `https://medium.com/@nikomanousos123/advanced-local-file-inclusion-leveraging-php-filters-when-standard-injection-fails-81de4f661f74`

and the payload I use is

```
?file=php://filter/read=convert.base64-encode/resource=flag.php
```

Next I put it into the page parameters section and this is what I got.

<img width="500" height="500" alt="屏幕截图 2025-09-23 144018" src="https://github.com/user-attachments/assets/6f9aa217-34b1-4e4f-8bfc-64d09a7d90e8" />

I got a base64. which is the flag. then i decode it and i get it

<img width="300" height="185" alt="屏幕截图 2025-09-23 144139" src="https://github.com/user-attachments/assets/50e80090-3eca-4064-85b6-be286716e08f" />


## Flag

```
ITTSec{_cl4ss1c_Lfi_}
```

## Tools & Techniques

`LFI`
`PHP Filter`
`Base64`
`Bash`

---
*Writeup by yunx1ao - 2025-09-23*
