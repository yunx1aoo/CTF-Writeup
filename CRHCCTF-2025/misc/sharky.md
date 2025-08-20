<img width="617" height="471" alt="image" src="https://github.com/user-attachments/assets/4684ec9e-6ec2-49cc-9c3d-2cb89759eb79" />

# sharky - 100 points
**Description:** `Don't u love gura?`

**Attachments:** `gura.jpg`

**Hint:**

**Author:** `na`

---

![gura](https://github.com/user-attachments/assets/fb3571d7-6154-49c3-96dd-24d20f8ccaef)

I was given a waifu image, haha. To complete this challenge, we can use `Aperi Solve` or `ExifTool`. But here, I'm just using ExifTool.

```bash
 exiftool gura.jpg
```

and I found a description that seems to be a cipher

```bash
Description                     : ILYC{gg_z_a_mifd_ybrrq}
```

I noticed that it was a `vigenere cipher`. If I look again at the description that says `"Don't you love gura?"`, it's possible that the key used was `gura`.

We can use online tools to decrypt the cipher. The example I use is `cyberchef`.

**https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('gura')&input=SUxZQ3tnZ196X2FfbWlmZF95YnJycX0**

## **Flag:** `CRHC{am_i_a_good_shark}`
