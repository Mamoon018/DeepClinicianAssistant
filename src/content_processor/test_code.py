

"""
Creating Neo4j Connection:
1- Create instance on Neo4j.
2- Initialize the connection with Neo4j DB.

Building KG:
1- Get the entities_with_ids object.
2- Create the variables that we need to pass onto the cypher query. (For Nodes & Properties)
3- Write a cypher query for entities.
4- Apply for loop, that takes each object and executes cypher query for it.

Replicate this for relationships, with different cypher query.
"""

from utils import neo4j_dbconnection, neo4j_uri




## Testing 
if __name__ == "__main__":

    with neo4j_dbconnection() as driver:            
            driver.verify_connectivity()
            print("Connection successfully created!")

    #print(type(neo4j_uri))