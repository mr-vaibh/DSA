from operator import le
from os import path
import re
from tkinter.messagebox import NO
from turtle import st


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].add(end)
            else:
                self.graph_dict[start] = {end}
    
    def get_paths(self, start, end, _path=[]):
        path = _path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)

                for each_path in new_paths:
                    paths.append(each_path)
        return paths
    
    def get_shortest_path(self, start, end, _path=[]):
        path = _path + [start]

        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                new_shortest_path = self.get_shortest_path(node, end, path)

                if new_shortest_path:
                    if shortest_path is None or len(new_shortest_path) < len(shortest_path):
                        shortest_path = new_shortest_path
        
        return shortest_path
    
    def display_graph(self):
        for key, value in self.graph_dict.items():
            print(key, '-->', value)


routes = [
    ('Mumbai', 'Paris'),
    ('Mumbai', 'Paris'),
    ('Mumbai', 'Dubai'),
    ('Paris', 'Dubai'),
    ('Paris', 'New York'),
    ('Dubai', 'New York'),
    ('New York', 'Toronto'),
]

flights = Graph(routes)

flights.display_graph()
print(flights.get_paths('Mumbai', 'New York'))
print(flights.get_shortest_path('Mumbai', 'New York'))