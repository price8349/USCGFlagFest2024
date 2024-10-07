# Echoes of Evidence

There were three parts to this flag: the analyst's name, a source IP, and the password of the suspect.

It was really easy to fall down a rabbit hole here, as Autopsy would show you a Word document with the challenge author's name. I tried that name in the flag a lot more than I would like to admit, before realizing it was as simple as the name of the analyst's home directory - garblyx.

Then, you had to open up the PCAP file at /home/garblyx/Work/ice cream.pcap, which contained an FTP transfer of a windows.zip from the IP 4.246.129.165 (the source IP). 

Then you can export this ZIP file via Wireshark (File -> Export Objects -> FTP-DATA), take the SAM and SYSTEM registry hives from this windows.zip (Windows\System32\config\SYSTEM and Windows\System32\config\SAM), run the hives through impacket-secretsdump, then use Hashcat or a site like Hashes.com to crack the hash for the Bob user. The resulting password is constantine.
```
$ impacket-secretsdump LOCAL -system SYSTEM -sam SAM
Impacket v0.12.0.dev1 - Copyright 2023 Fortra

[*] Target system bootKey: 0x3e1d0838f58f3b1fa36945c85de70db9
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:93fc568ca147bd24374f4798eacfa6cc:::
Bob:1001:aad3b435b51404eeaad3b435b51404ee:04fbd2397bc4b704927713c8d9e9ec81:::
[*] Cleaning up... 
```
Flag: FFCTF{garblyx_4.246.129.165_constantine}