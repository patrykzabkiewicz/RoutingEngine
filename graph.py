#!/usr/bin/env python

class Graph:
	def __init__(self):
		self.data = []

	def generate_edges(self, graph):
		edges = []
		for node in graph:
			for neighbour in graph[node]:
				edges.append((node, neighbour))

		return edges
