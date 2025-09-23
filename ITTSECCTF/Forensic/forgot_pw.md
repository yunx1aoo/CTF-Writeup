# Forgot Password

<img width="300" height="300" alt="屏幕截图 2025-09-21 212956" src="https://github.com/user-attachments/assets/a3743a98-8275-45af-b80d-e2c74796b621" />

---

**Category:** `Forensic`

**Description:**
```
Teman saya lupa passwordnya, yang dia ingat 8 karakter (Uppercase, Number).
Tolong bantu pecahkan, terimakasih dan youRock!
Note: Format Flag: ITTSec{passwordnya}
Jangan bruteforce ke server! Tombol Submit Flag akan terkunci/disable jika salah 5 kali
```

**Attachments:** `handshake_ITTSec_7A-76-18-23-9F-91_2025-09-08T13-56-54.cap`

**Difficulty:**

**Points:** `12`

**Author:**

**Date:** 2025-09-23

---

## Solution

given a .cap file. if we look at the file type it uses file. 

<img width="1876" height="107" alt="image" src="https://github.com/user-attachments/assets/b0c21c92-2a0e-4048-a07f-0e92de945cd2" />

there is a number `802.11` <- this is a number for a set of standards developed by someone, I've forgotten, but it's definitely in the wifi network.

In short, since this is WiFi, we can use `AirCrack` to get the password. Furthermore, if you look closely at the description, it says something like `"youRock!"`, which indirectly refers to Rockyou. It seems we'll have to resort to brute force.

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/1fa8ff59-b05d-4294-b43c-1d44774f84d4" />

Brute force has been performed. We can wait for a while. It seems like someone is trying to connect to wifi with SSID `7A:76:18:23:9F:91`

After waiting for almost 10 minutes, finally. It was really tiring.

<img width="500" height="500" alt="屏幕截图 2025-09-23 163748" src="https://github.com/user-attachments/assets/3d85ea83-484f-4fde-ab96-338ee7134e9a" />


## Flag

```
ITTSec{GOGETME1}
```

## Tools & Techniques

`aircrack-ng`

---
*Writeup by yunx1ao - 2025-09-23*
