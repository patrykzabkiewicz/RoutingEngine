#!/usr/bin/env python
""" Edge Class
Represent a edge of the graph with properties.

Author: 	Patryk Zabkiewicz
Date:		2015.08.03

"""

class Edge:
    def __init__(self,edge=""):
        self.capacity = edge.capacity
        self.flow = edge.flow
        self.lenght = edge.lenght
        self.speed = edge.speed
        self.cost = edge.cost
