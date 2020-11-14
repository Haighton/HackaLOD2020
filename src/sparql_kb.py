#!/usr/bin/env python3
""" HackaLOD 2020

Documentatie SPARQL endpoint data.bibliotheken.nl:
http://data.bibliotheken.nl/files/hulptekst_data.bibliotheken.nl.pdf
"""

# import rdflib
from SPARQLWrapper import SPARQLWrapper, XML

# Set SPARQL endpoint.
sparql = SPARQLWrapper('http://data.bibliotheken.nl/sparql')

# Define a SPARQL query
sparql.setQuery("""
    SELECT DISTINCT ?predicaat
    WHERE {
        ?subject a schema:Book .
        ?subject ?predicaat [] .
    }
""")

sparql.setReturnFormat(XML)
results = sparql.query().convert()

"""
# Extract values from JSON.
for result in results['results']['bindings']:
    print(result['Concept']['value'])
"""

# Save to XML file.
xml_file = results.toxml()
f = open('../data/alle_predicaten_boeken.xml', 'w')
f.write(xml_file)
f.close()


print(xml_file)
