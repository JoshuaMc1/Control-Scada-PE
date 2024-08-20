@ -------------------------
@ ----- Data section -----
@ -------------------------

.data
.balign 4
pin2: .int 2
pin3: .int 0
OUTPUT = 1
filePath: .asciz "/home/sps/examen/status/status.txt"
statusMsg: .asciz "0\n"

@ ---------------------------
@  ----- code Section -----
@ ---------------------------

.text 
.global main
.extern printf
.extern wiringPiSetup
.extern digitalWrite
.extern pinMode

main:   
    push {ip, lr}

    bl wiringPiSetup

    @ Configurar GPIO 2 como salida
    ldr r0, =pin2
    ldr r0, [r0]
    mov r1, #OUTPUT
    bl pinMode

    @ Configurar GPIO 3 como salida
    ldr r0, =pin3
    ldr r0, [r0]
    mov r1, #OUTPUT
    bl pinMode

    @ Encender GPIO 2
    ldr r0, =pin2
    ldr r0, [r0]
    mov r1, #1
    bl digitalWrite

    @ Apagar GPIO 3
    ldr r0, =pin3
    ldr r0, [r0]
    mov r1, #0
    bl digitalWrite

    @ Open the file
    ldr r0, =filePath
    mov r1, #577               @ O_WRONLY | O_CREAT | O_TRUNC
    mov r2, #438               @ S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH
    mov r7, #5                 @ sys_open
    svc 0

    @ Save file descriptor
    mov r4, r0

    @ Write the status to the file
    ldr r0, [r4]
    ldr r1, =statusMsg
    mov r2, #2                 @ Length of "0\n"
    mov r7, #4                 @ sys_write
    svc 0

    @ Close the file
    mov r0, r4
    mov r7, #6                 @ sys_close
    svc 0

    pop {ip, pc}
