# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:28:13 2021

@author: rafsh
"""

name= ['Rafshan','Bin','Razzak'];

print(name);

name.append('Mahi');
print(name);

name.insert(2, 'habijabi');

print(name);

name.pop(2);

print(name);

print(len(name));

number=[1,51,8,16,7,5];

lst=number[1:4];

print(lst);

lst=number[1:];

print(lst);


i=0
while i<=10:
    i=i+1;
    if i==6:
        
        continue
    print(i);
    
    
    
    
for item in range(0,100):
    print(item);
    
    
    
        
for item in range(0,100,10):
    print(item);