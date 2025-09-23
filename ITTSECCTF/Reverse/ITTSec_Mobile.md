# ITT sec Mobile

<img width="300" height="300" alt="屏幕截图 2025-09-21 213006" src="https://github.com/user-attachments/assets/8ae798a9-674c-4c5a-8f9e-f5643d79d04d" />

---

**Category:** `Mobile Rev`

**Description:**

**Attachments:** `ittsec1.apk`

**Difficulty:**

**Points:** `13`

**Author:**

**Date:** 2025-09-23

---

## Solution

I don't know if this is the way the committee wants to solve it. Because I think it's a bit unreasonable for me to get a flag just like this.

```bash
strings itsec.apk | grep -a ITT
```

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/8c5ba064-ae73-4048-b322-bde23da89f27" />


## Flag

```
ITTSec{e4sy_r3ver53_Flag_s0}
```

## Tools & Techniques

`grep`
`strings`

---
*Writeup by spl1t4t3rminal - 2025-09-23*
