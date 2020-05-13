'''
将 "Don't panic!" 转换成 "on tap"
'''

phrase = "don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

# -----

'''没有改变 plist'''

phrase = "don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5],plist[4],plist[7],plist[6]])

print(plist)
print(new_phrase)


# ----


phrase = "Don't panic!"
plist = list(phrase)
print(phrase) 
print(plist)

new_phrase = ''.join(plist[1:3]) + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)
