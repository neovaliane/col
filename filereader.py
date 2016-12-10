#!/usr/bin/env python3
name=input('File name?')
print(name)
text=open(name,'r')
text
line_count=0
word_count=0
char_count=0
for line in text:
   line_count+=1
   word_count+=len(line.split())
   char_count+=len(line)
print(line_count, word_count, char_count)

         

