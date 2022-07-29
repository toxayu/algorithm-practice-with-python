# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:39:02 2017

@author: surface
"""

class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
    
class Contact:
    all_contacts = ContactList()
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
        Contact.all_contacts.append(self)
        
class Role(Contact):
    def indicate(self):
        print('{} is {}'.format(self.name, self.number))
        
class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest
    
class Friend(Contact):
    def __init__(self, name, number, phone):
        super().__init__(name, number)
        self.phone = phone
        
        
class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.name)
        
class EmailableContact(Contact, MailSender):
    pass