# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 09:59:35 2017

@author: surface
"""

import numpy as np

def Magic(N,i_init,j_init):
    
    Square = [[0]*N for row in range(N)]
    
    
    for step in range(N**2):
        Square[i_init][j_init] = step + 1
        print(i_init,j_init,step+1)
        i_next = i_init - 1
        j_next = j_init - 1
        
        if i_next < 0:
            i_next += N
        if j_next < 0:
            j_next += N
        
           
        if Square[i_next][j_next] != 0:
         
           i_next = i_init + 1
           j_next = j_init
           
        elif j_next >= N:
           break
     
            
        
            
        i_init = i_next
        j_init = j_next
            
    Square = np.array(Square)
    return Square
            
        
        
        
        