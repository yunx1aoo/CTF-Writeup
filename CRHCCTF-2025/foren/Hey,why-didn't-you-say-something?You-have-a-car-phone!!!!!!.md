<img width="300" height="300" alt="1_fhXqUhHDLGXcQaRAaKyecw" src="https://github.com/user-attachments/assets/b73dd18c-fa36-4dbd-8390-ff86e14deb0a" />

# Hey,why-didn't-you-say-something?You-have-a-car-phone!!!!!! - 100

**Description:** `0011000A81908878776600000B304676F80C4ACF41C4F29C9E7687E9E9B71BE4ACB7C5653928EC2683B07A2BDD8915AEC9D65C5B4C94BA5D
CRHC{asnwer}` 

**Attachments:**

**Hints:**

**Author:** `夜有夢`
---

we are given some like hex but thast not a hex. but if i identify this is a pdu SMS. because SMS use hex to encrpyt their message. to solve this we can use `PDU SMS Decoder` like this -> `https://www.smsdeliverer.com/online-sms-pdu-decoder.aspx`

if we paste that hex to the decoder tools we can find this

[cyberchef]: https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=WHpWdE5YQmtkVjltYkRSbi4

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/40845d83-719d-45bb-98b2-8902e09debdf" />

**To**:	`0988877766`

**Message**:	`Flag is Destination Number and XzVtNXBkdV9mbDRn.`

the message said that. `flag is destination and XzVtNXBkdV9mbDRn.`

`XzVtNXBkdV9mbDRn.` <- this string like a base64. so i decode thas using [cyberchef] and get this string flag

<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/e77864d6-d520-4e84-ab3c-7a54fd9efa50" />

so the final flag is:

## **flag:** `CRHC{0988877766_5m5pdu_fl4g}`
