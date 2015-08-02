#!/usr/bin/env python

from graph import *

if __name__ == "__main__":
	   	graph1 = { "a" : ["c", "a"],
			  "b" : ["c", "e", "d"],
			  "c" : ["a", "b", "d", "e"],
			  "d" : ["c"],
			  "e" : ["c", "b"],
			  "f" : []
			}

		g = Graph(graph1)
		print(g.generate_edges())
