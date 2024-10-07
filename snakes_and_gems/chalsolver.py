import base64

c = open("challenge.py","rb").read().split(b"\n")

py_prefix = b"E="
ruby_prefix = b'B="'
stage = 1
while True:
	if stage > 100: break
	solved = False
	for i in c:
		if i.startswith(py_prefix):
			b = i.replace(py_prefix,b"").replace(b"'",b"")
			c = base64.b64decode(b).split(b"\n")
		elif i.startswith(ruby_prefix):
			b = i.replace(ruby_prefix,b"").replace(b'"',b"")
			c = base64.b64decode(b).split(b"\n")
		elif i.startswith(b'I="') or i.startswith(b'Z="'):
			print(i.decode().replace('I="','').replace('Z="','').replace('"',''))

	stage += 1
print(b"\n".join(c).decode("utf-8"))