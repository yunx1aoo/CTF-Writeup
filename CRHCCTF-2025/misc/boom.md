<img width="618" height="625" alt="屏幕截图 2025-08-20 083208" src="https://github.com/user-attachments/assets/ef2c37cd-78c8-4a4c-8491-c61c819004e8" />

---
# boom - 100 points
**Description:** `booooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooom`
**attachments:** `boom.MP4` `boom.zip`

**Hint:**
> boom.mp4 is useless, I just wanted to show it to everyone

---
we are given a video file `boom.MP4` and there is also a zip file `boom.zip`. When I opened the mp4 file, I got a video that seemed to be a Chinese song. There was nothing that interesting in it. that's why i switched to the zip file. when i extracted the zip
```bash
unzip boom.zip
```
<img width="1882" height="945" alt="屏幕截图 2025-08-20 084234" src="https://github.com/user-attachments/assets/d3eb0ce3-ff31-4dc3-bd50-f5bdc3ca1162" />

oh my god. why are there so many layers haha. we can't possibly open every layer just to get the flag. this is impossible lol

---
# solution
We can use the `-r` option in `grep` to recursively search our current directory. Using this option will make searching much easier. We can use the format flags to aid in the search.

.

```bash
grep -r 'CRHC'
```

<img width="770" height="129" alt="屏幕截图 2025-08-20 085346 - Copy" src="https://github.com/user-attachments/assets/6d2afec3-fa87-4704-8541-c145b40f014d" />

and yeah haha. we got it

## **Flag:** `CRHC{ㄒㄧㄡ~ㄅㄥˋ~ㄒㄧㄡ~ㄅㄥˋㄒㄧㄡㄒㄧㄡㄅㄥˋㄅㄥˋ放煙火}`
