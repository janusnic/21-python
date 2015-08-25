an_image = open('examples/beauregard.jpg', mode='rb')
print(an_image.mode)
print(an_image.name)
# print(an_image.encoding) # a binary stream object has no encoding attribute

print(an_image.tell()) # 0

data = an_image.read(3)

print(data)
print(an_image.tell()) # 3
an_image.seek(0)
data = an_image.read()
print(len(data)) # 3150
