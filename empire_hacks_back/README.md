# Empire Hacks Back

This is a format string/buffer overflow attack. First, I reverse engineered the binary to find the password (Force2024).
The buffer for the numeric value is 1 byte, but the program reads more than that, and you can overflow into the username buffer, which is used in a printf call.
I bruteforced pointers with 1%n$x (you must prefix with a valid option, hence the 1 at the start) after attaching to GDB to find where the flag was allocated. 1%18$x gave me the flag pointer, and then running 1%18$x on the remote machine gave me the flag.