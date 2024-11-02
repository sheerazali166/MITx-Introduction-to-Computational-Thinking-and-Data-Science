#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:20:59 2024

@author: sheeraz
"""

# Program 7


class Node(object):
    
    def __init__(self, name):
        
        """Assumes name is a string"""
        self.name = name
        
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    
        
class Edge(object):
    
    def __init__(self, src, dest):
        
        """Assumes src and dest are nodes"""
        
        self.src = src
        self.dest = dest
       
        
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() + "->" + self.dest.getName() 
        

class Diagraph(object):
    
    """edges is a dict mapping each node node a list of
       its children"""
       
    def __init__(self):
        self.edges = {}
        
    def addNode(self, node):
        
        if node in self.edges:
            raise ValueError("Duplicate node")
        else:
            self.edges[node] = []
     
    def addEdge(self, edge):
        
        src = edge.getSource()
        dest = edge.getDestination()
        
        if not (src in self.edges and dest in self.edges):
            raise ValueError("Node not in graph")
            
        self.edges[src].append(dest)
        
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    
    def getNode(self, name):
        
        for n in self.edges:
            
            if n.getName() == name:
                return n
            
        raise NameError(name)
        
        
    def __str__(self):
        
       result = ""
       
       for src in self.edges:
           for dest in self.edges[src]:
               
               result = result + src.getName() + "->" + dest.getName() + "\n"
       
       return result[:-1] # omit final newline       
           
       
class Graph(Diagraph):
    
    def addEdge(self, edge):
        
        Diagraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Diagraph.addEdge(self, rev)
        
def buildCityGraph(graphType):
      g = graphType()
      
      
      for name in ("Boston", "Province", "New York",
                       "Chicago", "Denver", "Phoenix", "Los Angles"): # create 7 nodes
          g.addNode(Node(name))
          
   
      g.addEdge(Edge(g.getNode("Boston"), g.getNode("Province")))
      g.addEdge(Edge(g.getNode("Boston"), g.getNode("New York")))
      g.addEdge(Edge(g.getNode("Province"), g.getNode("Boston")))
      g.addEdge(Edge(g.getNode("Province"), g.getNode("New York"))) # illigal puppies want this
      g.addEdge(Edge(g.getNode("New York"), g.getNode("Chicago"))) # becomes this
      g.addEdge(Edge(g.getNode("Denver"), g.getNode("Phoenix")))
      g.addEdge(Edge(g.getNode("Denver"), g.getNode("Denver")))
      g.addEdge(Edge(g.getNode("Los Angles"), g.getNode("Boston")))
      
      return g
  
    

print(buildCityGraph(Graph))





      
      
           
         
         
            
            
            
            
            
            
            
            
                
         
        
        
            
             
            
        
        
        
                
            
            
            
            
            

            
       
       
    
    
    
    
    
    
        
        
        
        
    
    
        