# Crystal Clear

This was a reversing challenge in the Crystal programming language.

There was an XOR and array assignment:
```x86asm
mov     edi, 45h ; 'E' ; 0x45 = 69
call    _Random__new_Int32__Random__PCG32
; ...
mov     rbx, [r15]
mov     rdi, [r13+0]
mov     esi, 36Eh
call    _Random__PCG32@Random_rand_UInt8_class__UInt8
movzx   esi, al
mov     rdi, rbx
call    _Array_Int32_@Array_T_____Int32__Array_Int32_
dec     ebp
jnz     short loc_52D80```

```x86asm
mov     esi, 20h ; ' '
call    _Array_Int32_@Array_T___unsafe_build_Int32__Array_Int32_
mov     rbx, rax
mov     r15, [rax+10h]
xor     ebp, ebp
mov     rdi, r15
xor     esi, esi
mov     edx, 0B7h
call    _Pointer_Int32_@Pointer_T______Int32__Int32__Int32
mov     rdi, r15
mov     esi, 1
mov     edx, 0E2h
call    _Pointer_Int32_@Pointer_T______Int32__Int32__Int32```

The script at `final.cr` will decrypt the buffer in the program.