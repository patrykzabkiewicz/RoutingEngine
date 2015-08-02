#!/usr/bin/env python
""" Graph Class
Base class for routing engine.

Author: 	Patryk Zabkiewicz
Date:		2015.08.01

"""

class Graph:
	def __init__(self,graph_input={}):
		self.__graph = graph_input

	def add_vertex(self,vertex):
		if vertex not in self.__graph:
			self.__graph[vertex] = []

	def add_edge(self,edge):
		edge = set(edge)
		(vertex1, vertex2) = tuple(edge)
		if vertex1 in self.__graph:
			self.__graph[vertex1].append(vertex2)
		else:
			self.__graph[vertex1] = [vertex2]

	def generate_edges(self):
		edges = []
		for node in self.__graph:
			for neighbour in self.__graph[node]:
				edges.append((node, neighbour))
		return edges

	def find_isolated_nodes(self):
		isolated = []
		for node in self.__graph:
			if not self.__graph[node]:
				isolated += node
		return isolated
