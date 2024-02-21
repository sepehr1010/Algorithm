#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jan 10 12:26:03 2024

@author: sefat07
"""
class vertex:
    
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        
    def addNeigh(self, nbr, weight):  
        self.connectedTo[nbr] = weight
            
    def getConn(self):
        return self.connectedTo.keys()
    
    def conn(self):
        return [x.id for x in self.connectedTo]
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

v1 = vertex(3)
v2 = vertex(6)

v1.addNeigh(v2, 1)

v1.connectedTo

v1.getConn()

v1.conn()

v1.getWeight(v2)

#%%%%%%%%%%


class graph:
    
    def __init__(self):
        self.nodes = {}
        
    def addVertext(self, vert):
        self.nodes[vert] = vertex(vert)
    
    def addEdge(self, fromVert, toVert, weight):
        if fromVert not in self.nodes.keys(): # same as self.nodes:
            self.addVertext(fromVert)
        if toVert not in self.nodes:
            self.addVertext(toVert)        
        self.nodes[fromVert].addNeigh(self.nodes[toVert], weight)
    
    def getVertex(self, vertKey):
        return self.nodes[vertKey]
    
    
g = graph()
g.addVertext(3)  
g.getVertex(3)


#g.addVertext(6)   
g.addEdge(3, 6, 2)  
g.getVertex(3).conn()   
    
#%%%%%%%%%%%%%%%

class stack:
    def __init__(self):
        self.items = []
    def addMemmber(self, *item):
        for i in item:
            self.items.append(i)
    def delMember(self, item):
        self.items.remove(item)
    def show(self):
        return self.items
    def __call__(self):
        return self.items
    def __len__(self):
        return len(self.items)
    def __getitem__(self, item):
        return self.items[item]
    
a= stack()
a.addMemmber(0, 2, 3)
a.items 
    
    
    
    
    
    
    
    
    
    
        