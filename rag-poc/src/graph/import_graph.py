\"\"\"Bulk CSV import helper for Neo4j knowledge graph\"\"\"
import csv
from py2neo import Graph

def import_graph(node_csv, rel_csv):
    graph = Graph('bolt://localhost:7687', auth=('neo4j','password'))
    # TODO: load CSV files into Neo4j via bulk import or LOAD CSV Cypher
    pass

if __name__ == '__main__':
    import_graph('nodes.csv', 'rels.csv')
