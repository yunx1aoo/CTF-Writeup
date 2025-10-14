# Flag in Flame

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/523947c2-ca50-4f8a-9345-af2b52b2c65d" />

**Tag:** `Forensics` `browser_webshell_solvable`

**Description:** 
> The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log. Download the encoded data here: Logs Data. Be prepared—the file is large, and examining it thoroughly is crucial .

**Attachments:** `logs.txt`

**Hints:**

<details>
<summary>Hint 1</summary>

Use base64 to decode the data and generate the image file.

</details>

**Author:** Prince Niyonshuti N.

**Solved:** `1.084 users solved`

---

# Solution

<img width="1000" height="500" alt="屏幕截图 2025-10-14 113119" src="https://github.com/user-attachments/assets/3870a58d-a0e4-41ea-9a13-f3ac9d940681" />

we are given a very very very long base 64 encoding 🗿. if we decode it. then it will give this output

<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/2ae728b0-e058-4716-845b-74ca629d51c9" />

We can see that at the very top there is a prefix for PNG. Well, the hint says that we have to convert the base64 to an image. So next, we add "add text to image" in Cyberchef. like this

<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/30045328-f17e-4a2f-8738-ec2587955a72" />

you can see i scrolled to the bottom of the image and got a hex. Next we take the hex and then decrypt it all and get the flag

<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/d33b6e07-a682-450f-bffd-d7150a1c7a52" />

# FLAG: picoCTF{forensics_analysis_is_amazing_be860279}
