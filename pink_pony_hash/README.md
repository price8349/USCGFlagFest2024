# Pink Pony Hash

This was a hash length extension attack. The source is in index.php, but this is what we're looking for:
```php
assert(strlen($secret) == 19);
function make_cookie() {
    global $secret;

    $payload = "kitty_cat";
    setcookie("token", base64_encode($payload) . "." . sha1($secret . $payload));
    header("Location: /"); //reload page
    exit(); //we're done
}
// ...
if(strstr($payload, "pink_pony")) {
    $flag = "FFCTF{Th!\$_iS_4_Fl@g}";
    echo "<h1>OMG A MEMBER OF THE PINK PONY CLUB?! HERES UR FLAG: $flag</h1>";
}else{
    echo "<h1>sry we only give flags to members of the pink pony club, not $payload :c</h1>";
}
```

I solved this using the tool [hash_extender](https://github.com/iagox86/hash_extender):
```
$ ./hash_extender \
    -f sha1 \
    -d "kitty_cat" \
    -l 19 \
    -s 8665c860a93878c794775cafcafeea6e9f05476a \
    -a pink_pony
Type: sha1
Secret length: 19
New signature: ef06417fa3a9de7eb0d48a5f21274926c207d8a1
New string: 6b697474795f6361748000000000000000000000000000000000000000000000000000000000000000000000e070696e6b5f706f6e79
```