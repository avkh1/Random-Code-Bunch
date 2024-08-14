; NASM
; Printing all the ASCII

section .data
    ; Define the space character
    space db 0x20

section .bss
    ; Define the initial character to be printed (space, 0x20)
    char resb 1

section .text
    global _start

_start:
    ; Initialize the character to space (0x20)
    mov byte [char], 0x20

print_loop:
    ; Set up registers for sys_write
    mov rax, 1          ; sys_write system call number (1)
    mov rdi, 1          ; File descriptor 1 is stdout
    lea rsi, [char]     ; Pointer to the character to print
    mov rdx, 1          ; Length of 1 byte (1 character)
    syscall             ; Write the character

    ; Print a space after the character
    lea rsi, [space]    ; Pointer to the space character
    mov rdx, 1          ; Length of 1 byte (1 space)
    syscall             ; Write the space

    ; Move to the next character
    inc byte [char]     ; Increment the character
    cmp byte [char], 0x7E ; Compare with '~' (0x7E)
    jbe print_loop      ; If less than or equal to '~', repeat loop

    ; Exit the program
    mov rax, 60         ; sys_exit system call number (60)
    xor rdi, rdi        ; Exit code 0
    syscall
