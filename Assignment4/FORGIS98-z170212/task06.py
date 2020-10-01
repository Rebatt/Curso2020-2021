# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hSv61ejXESrp34CUz1PqZCsoA43tzc8y

**Task 06: Modifying RDF(s)**
"""

# !pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, XSD
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""
**TASK 6.1: Create a new class named "University"**

**TASK 6.2: Add "Researcher" as a subclass of "Person"**

**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**

**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**

**TASK 6.5: Add UPM as the university where John Smith works**
"""

# TASK 6.1
print("\nTASK 6.1")
g.add((ns.University, RDF.type, RDFS.Class))
for subj, pred, obj in g.triples((ns.University, None, None)):
  print(subj, pred, obj)

# TASK 6.2
print("\nTASK 6.2")
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for subj, pred, obj in g.triples((None, RDFS.subClassOf, None)):
    print(subj, pred, obj)

# TASK 6.3
print("\nTASK 6.3")
g.add((ns.JaneSmith, RDF.type, ns.Researcher))
for subj, pred, obj in g.triples((ns.JaneSmith, None, None)):
    print(subj, pred, obj)

# TASK 6.4
print("\nTASK 6.4")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
g.add((ns.JaneSmith, vcard.FN, Literal("Jane Smith", datatype=XSD.string)))
g.add((ns.JaneSmith, vcard.Given, Literal("Jane", datatype=XSD.string)))
g.add((ns.JaneSmith, vcard.Family, Literal("Smith", datatype=XSD.string)))
for subj, pred, obj in g.triples((ns.JaneSmith, None, None)):
    print(subj, pred, obj)

# TASK 6.5
print("\nTASK 6.5")
g.add((ns.UMP, RDF.type, ns.University))
g.add((ns.JaneSmith, ns.Work, ns.UPM))
for subj, pred, obj in g.triples((ns.JaneSmith, ns.Work, None)):
    print(subj, pred, obj)
for subj, pred, obj in g.triples((ns.UPM, None, None)):
    print(subj, pred, obj)
