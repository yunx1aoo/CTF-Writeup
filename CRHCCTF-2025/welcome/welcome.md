# Welcome - 100 points
**Description:** 
`Hello guys! This is the very first CTF competition hosted by CRHC, Kaohsiung Municipal Hsin Chuang Senior High School Computer Research Club! The overall difficulty is beginner-friendly, and we've even invited several elite hackers as our challenge creators — huge thanks to all of them! 🙏 🏆 Top 3 winners will get a free drink from me! (Also, our club president and I are sponsoring Discord Nitro for the top 3!) 🚨 Eligibility: Limited to students from Kaohsiung Municipal Hsin Chuang Senior High School or nearby schools (must be within reasonable distance). 🍹 Guaranteed slot: At least 1 winner from Kaohsiung Municipal Hsin Chuang Senior High School is guaranteed! 🤝 If you bump into me in person, feel free to claim your reward — wink wink 😏 Flag format: CRHC{...} flag:Q1JIQ3t3ZWxjMG1lXzJfdGhlX2ZpcnN0X2N0ZiF9==`

**attachments:** 

---
We are given a `base64`. We can immediately decode it using `Linux`.

```bash
echo 'Q1JIQ3t3ZWxjMG1lXzJfdGhlX2ZpcnN0X2N0ZiF9==' | base64 -d
CRHC{welc0me_2_the_first_ctf!}
```

## **flag:** `CRHC{welc0me_2_the_first_ctf!}`
