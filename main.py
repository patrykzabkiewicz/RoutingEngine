#!/usr/bin/env python

from graph import *

if __name__ == "__main__":
	   	g1 = { "a" : ["c", "a"],
			  "b" : ["c", "e", "d"],
			  "c" : ["a", "b", "d", "e"],
			  "d" : ["c"],
			  "e" : ["c", "b"],
			  "f" : []
			}

		g = Graph()
		print(g.generate_edges(g1))
