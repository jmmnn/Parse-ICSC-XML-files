import xml.etree.ElementTree as ET

# The result will be stored here
values = []

#Parsing the XML file
tree = ET.ElementTree(file='pac_DSID_xml.xml')
root = tree.getroot()
print 'root tag : ' , root.tag
print 'root attrib : ' , root.attrib

# for child in root:
#     print child.tag, child.attrib

# this finds the 1st dataXML instance
#print 'mis pruebas' , root[1][0].tag, root[1][0].attrib

# this finds the 1st inside dataXML instance
#print 'ds_id tag:' , root[1][0][0].tag, '   ds_id text:' , root[1][0][0].text, '    ds_id attrib:' , root[1][0][0].attrib

# #this works basic
# for dataXML in root.iter('dataXML'):
#     print dataXML[0].tag , dataXML[0].text

#this works to create a dict per row - however will fail if values are missing
for dataXML in root.iter('dataXML'):
    dicto = {dataXML[0].tag : dataXML[0].text, dataXML[1].tag : dataXML[1].text , dataXML[2].tag : dataXML[2].text, dataXML[3].tag : dataXML[3].text }
    #print dicto
    values.append(dicto)


# # this works but has too many lists
# for dataXML in root.iter('dataXML'):
#     renglon = []
#     for i in range(0, len(dataXML)):
#         item = {}
#         item[i] = {dataXML[i].tag : dataXML[i].text}
#         renglon.append(item[i])
#     print renglon


#format as JSON
import json
print json.dumps(values)