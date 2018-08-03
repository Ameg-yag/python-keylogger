#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

class encryptor:
    def __init__(self , key ):
        self.key , self.iv  = self.initKey(key)
        self.mode =  AES.MODE_CBC
        
        self.encryptor = AES.new(self.key)
        
        
    def initKey(self , key):
        possibleValue = (16 , 24 ,32)
        lenght = len(key)
        
        convertoLengh = 0 
        for i in range(len(possibleValue)):
            if lenght > possibleValue[i]:
                pass
            else:
                convertoLengh = possibleValue[i]
                #print(possibleValue[i])
                break
        
        while len(key) < convertoLengh:
            key += " " 
        
        IV = '\x00' * convertoLengh
        return key  , IV 
    
    def encrypt(self , text):
        
        while len(text) % len(self.key) !=0 : 
            text += " " 
        
        print("Will Encrytp ->" , text )
        
        return self.encryptor.encrypt(text)
        
    def decrypt(self , text):
        
        return self.encryptor.decrypt(text)
    
