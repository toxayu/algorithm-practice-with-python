# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:34:23 2017

@author: surface
"""

class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0
        '''
        Initialize the bank account. You have to input the original amount and the name.
        
        
        '''
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('must be positive')
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError('balance not enough')