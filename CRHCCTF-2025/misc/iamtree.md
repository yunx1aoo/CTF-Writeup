<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/90e14a42-9b1a-4d06-9bcf-f783243251e6" />

# I AM A TREE - 100 points

**Description**: `I planted a tree yesterday, and I named it "hey". You know what a tree has? branches and leaves !`

**Attachments:** `hey.zip`

**Hints:**

**Author:** `na`

---

We are given a zip file `hey.zip`. We will extract this zip first.

```bash
unzip hey.zip
Archive:  hey.zip
   creating: hey/
   creating: hey/.git/
   creating: hey/.git/logs/
  inflating: hey/.git/logs/HEAD
.......
```

a hey folder comes out which contains `git`

let's move to that directory

```bash
cd hey
```

to complete this challenge quickly we can use this

```bash
git log --all --p
```

and there will be a lot of log output and there will be a flag like this

```bash
commit a8a9ab9aa5d0f9a54eeaadcf06bcc430ce353093 (flag-branch)
Author: flag{heyheyhey} <flag{lie}>
Date:   Thu Aug 7 04:52:55 2025 -0400

    Add FLAG.txt

diff --git a/FLAG.txt b/FLAG.txt
new file mode 100644
index 0000000..713c84c
--- /dev/null
+++ b/FLAG.txt
@@ -0,0 +1 @@
+CRHC{heyheyhey_9_8_77777}
```

or if you just want to flag it directly, we can use `grep` too

```bash
git log -all -p | grep CRHC{
```

## **Flag:** `CRHC{heyheyhey_9_8_77777}`
