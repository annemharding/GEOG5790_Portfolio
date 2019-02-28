# -*- coding: utf-8 -*-
"""
Anne Harding, 28/02/2019
GEOG5790 - Practical 6 (XML)
Script to validate, parse, write and transform XML.
"""

# Import modules:
from lxml import etree

'''
PART ONE - VALIDATING
'''
# Open dtd file:
dtd_file = open("map1.dtd")

# Open xml file and remove prologue:
xml1 = open("map1.xml").read()
xml1 = xml1.replace('<?xml version="1.0" encoding="UTF-8"?>',"")

# Validate xml file using dtd file:
dtd = etree.DTD(dtd_file)
root = etree.XML(xml1)
print(dtd.validate(root))

'''
PART TWO - PARSING AND ADDING
'''
# Parsing to list elements of the xml file:
root = etree.XML(xml1)		# Where xml1 is XML text
print (root.tag)			# "map"
print (root[0].tag)			# "polygon"
print (root[0].get("id"))	# "p1"
print (root[0][0].tag)		# "points"
print (root[0][0].text)		# "100,100 200,100" etc.

# Adding new polygon to xml file:
root = etree.XML(xml1)				# Could start from nothing
p2 = etree.Element("polygon")		# Create polygon
p2.set("id", "p2");					# Set attribute
p2.append(etree.Element("points"))	# Append points
p2[0].text = "100,100 100,200 200,200 200,100"	# Set points text
root.append(p2)						# Append polygon
print (root[1].tag)					# Check

# Write to a file:
out = etree.tostring(root, pretty_print=True)
print(out)
writer = open('map3.xml', 'wb')		# Open xml file for binary write
writer.write(out)                   # Write open to xml
writer.close()                      # Close writer

'''
PART THREE - TRANSFORMING 
'''
# Open newly created xml file and remove prologue:
xml3 = open("map3.xml").read()
xml3 = xml3.replace('<?xml version="1.0" encoding="UTF-8"?>',"")

# xml root:
root = etree.XML(xml3)

# Open xsl file and remove prologue:
xsl3 = open("map3.xsl").read()		# Read stylesheet
xsl3 = xsl3.replace('<?xml version="1.0" encoding="UTF-8"?>',"")

# Transform xml file to html:
xslt_root = etree.XML(xsl3)			# Parse stylesheet
transform = etree.XSLT(xslt_root)	# Make transform
result_tree = transform(root)		# Transform some XML root
transformed_text = str(result_tree) # Convert to string
print(transformed_text) 
writer = open('map3.html', 'w')		# Open html file to write
writer.write(transformed_text)      # Write transformed_text to html
writer.close()                      # Close writer