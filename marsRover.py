#!/usr/bin/env python
# -*-coding: iso-8859-9 -*-


from function import *
        
        
if True:                      
    dosya = raw_input("Okunacak dosyanın ismini giriniz" )
           
    if dosya:
        try:
            okuma(dosya + '.txt')
        except IOError:
            print "Dosya Bulunamadı!"

print konum.x, konum.y, konum.yon







