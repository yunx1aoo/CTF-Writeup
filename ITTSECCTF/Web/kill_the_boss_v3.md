# Kill The Boss V3

<img width="300" height="300" alt="屏幕截图 2025-09-21 212934" src="https://github.com/user-attachments/assets/8fba3b9c-5440-4fe5-bf33-0098d6ceaf7b" />

---

**Category:** `Web`

**Description:**

**Attachments:** `https://web4.ittsec.net/`


**Difficulty:**

**Points:** `10`

**Author:**

**Date:** 2025-09-23

---

## Solution

<img width="500" height="500" alt="屏幕截图 2025-09-21 213817" src="https://github.com/user-attachments/assets/6e387b35-7d81-4077-8453-bb1b8d8d6df1" />

we are given a never-ending fight between the minions and the dragon king again and again

<img width="500" height="500" alt="屏幕截图 2025-09-21 213827" src="https://github.com/user-attachments/assets/e4efb908-37da-4cff-befb-29d152d07772" />

If we click attack, as usual we are the ones who will always die, somehow this is so unfair.

This time the challenge is a bit different, when I checked the source code, it seems that our parameters have been encrypted using the encryption algorithm and there is also HMAC there.

<img width="500" height="500" alt="屏幕截图 2025-09-21 214255" src="https://github.com/user-attachments/assets/12c165dd-4057-45b0-9c48-0fd851243e74" />

<img width="500" height="500" alt="屏幕截图 2025-09-21 213839" src="https://github.com/user-attachments/assets/e344d556-7ba6-4771-b1b3-272612080e4c" />

because I saw that there were 2 interesting types of functions encryptedata(), and generatehmac() so I called them using the console

<img width="500" height="500" alt="屏幕截图 2025-09-21 214322" src="https://github.com/user-attachments/assets/9b7ba738-56cb-4ef5-a4eb-263a123ed8ab" />

<img width="500" height="500" alt="屏幕截图 2025-09-21 214326" src="https://github.com/user-attachments/assets/1c80e597-2171-46c4-8cb7-0322c8e89c6e" />

It was really unexpected that he would use the AES key algorithm there. After that, I tried brute force and searched for the AES key. And I found it.

<img width="675" height="93" alt="屏幕截图 2025-09-21 214416" src="https://github.com/user-attachments/assets/ed8becb0-a0b8-446b-a867-b6e45c7a4008" />

**key:** `MySuperSecretKey123`

Next I made a code to generate damage and a new hmac that I had set myself to beat the boss.

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/47449b3c-0138-46ff-bca4-347e58a26e92" />

```bash
(async () => {
const data = "damage-9001";
const enc = new TextEncoder();
const keyBytes = enc.encode(AES_KEY);
const iv = enc.encode(AES_IV);

const aeskey = await crypto.subtle.importKey('raw', keyBytes, {name: 'AES-CBC'}, false, ['encrypt']);
const ct = await crypto.subtle.encrypt({name: 'AES-CBC', iv}, aeskey, enc.encode(data));
const ct_b64 = btoa(String.fromCharCode(...new Uint8Array(ct)));

const mackey = await crypto.subtle.importKey('raw', keyBytes, {name: 'HMAC', hash: 'SHA-256'}, false, ['sign']);
const mac = await crypto.subtle.sign('HMAC', mackey, enc.encode(ct_b64));
const machex = [...new Uint8Array(mac)].map(b => b.toString(16).padStart(2,'0')).join('');

console.log(ct_b64, machex);
document.getElementById('encrypted_data').value = ct_b64;
document.getElementById('hmac_data').value = machex;
})();
```

we generate it via the console

<img width="500" height="500" alt="屏幕截图 2025-09-21 214658" src="https://github.com/user-attachments/assets/a860054e-8d73-4719-8778-296e83f287f5" />

Next, we replace the req data with the data that we will exploit.

<img width="500" height="221" alt="屏幕截图 2025-09-21 214903" src="https://github.com/user-attachments/assets/5eced591-4076-45d6-9c67-eef6526b6d19" />

the click send on burp suite

<img width="500" height="500" alt="屏幕截图 2025-09-21 215211" src="https://github.com/user-attachments/assets/9e9143fb-ba31-4265-bea6-eb7ad932c966" />

check the web and get it

## Flag

```
ITTSec{AES_crypt_4nd_HMAC_v3r1fy_ftw}
```

## Tools & Techniques

`burp suite`
`web parameter tempering`
`AES encrytpion`
`HMAC`
`Console`

---
*Writeup by spl1t4t3rminal - 2025-09-23*
