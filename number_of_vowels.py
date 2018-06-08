# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s='abecadaljldluoo'
count=0
for i in range(len(s)):
    if s[i] in ('a', 'o', 'i', 'e', 'u'):
        count +=1
    #if s[i]=="a" or s[i]=="e"  or s[i]=="i" or s[i]=="o" or s[i]=="u"
      #  count +=1
      #Why doesn't this work?
     
print('Number of Vowels: ' + str(count))


    

    