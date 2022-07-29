# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 09:50:50 2017

@author: surface
"""

class Contact:
    all_contacts = []
    
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)
        
    def __repr__(self):
        return "My name is " + self.name + ". My email is " + self.email + "."
        
class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        
class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone
        
    def __repr__(self):
        return "One of my friend is " + self.name