<img width="300" height="300" alt="屏幕截图 2025-08-20 111529" src="https://github.com/user-attachments/assets/fdda2ce4-65e1-4093-a83b-fadafbb434c7" />

# xor me - 100 point

**Description:** `Find the key and decode me`

**Attachments:** `output.txt`

**hint:**
> Always remember the flag format~~

**Author:** `Auron`

---
we are given a file called output.txt which contains the xor results

`3b623a0a0f316f16791a0c6f1927440f6f0521340c6f113b0d080742161d0b6f4316174c5e2d791a14492d2a06016f462c4c4d020f`

So this challenge asks us to find the key from the xor result and convert the xor result back to plaintext.

As far as I know, the general xor formula for finding a key is
> plain ^ cipher = key

There must be a question, how do we know the plaintext? In the hint, we are clearly told that we must remember the flag format. The flag format is CRHC{, this makes it easier to find the key used.

because it is hexdecimal, we will take the first 2 digits for testing, we can name it key1

like this example:
```python
>>> key1 = 0x3b ^ ord('C')
>>> print(key1)
120
>>> print(hex(key1))
0x78
```

That's the Python code that I use to get the key. We keep going from C to {. This means there are 5 keys that we will get. After I converted all of them, I got the candidates.
> 0x78
> 0x30
> 0x72
> 0x49
> 0x74

Well, now you've got it, let's just execute it. If you're my type and lazy to script, then we'll just use Cyber Chef. Put the from hex at the top and xor it, then in xor, select the hex and place it below the from hex

https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'78%2030%2072%2049%2074'%7D,'Standard',false)&input=M2I2MjNhMGEwZjMxNmYxNjc5MWEwYzZmMTkyNzQ0MGY2ZjA1MjEzNDBjNmYxMTNiMGQwODA3NDIxNjFkMGI2ZjQzMTYxNzRjNWUyZDc5MWExNDQ5MmQyYTA2MDE2ZjQ2MmM0YzRkMDIwZg&oeol=CR

## **Flag:** `CRHC{I_d0nt_kn0w_wh@t_cryp70_is_1_c4n_0nly_cry_4e852}`
