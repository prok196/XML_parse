import xml.etree.ElementTree as ET

mytree = ET.parse('Book.xml')
myroot = mytree.getroot()

dictx = {'a': 1, 'b': 2, 'c':3}
print(dictx.copy())

for i in myroot.findall('book'):
    id = i.attrib.get('id')
    author = i.find('author').text
    print (id, author)

