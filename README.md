Explanation for the DFS and BFS traversal for the graph.
Здійснено порівняння результатів алгоритмів для цього графа, пояснено різницю в отриманих шляхах. Обґрунтовано, чому шляхи для алгоритмів саме такі.

1.Result for DFS traversal from the starting point Bilbao:
[('Bilbao', 'Madrid'), ('Madrid', 'Barcelona'), ('Barcelona', 'Valencia'), ('Valencia', 'Seville'), ('Seville', 'Málaga'), ('Málaga', 'Granada'), 
('Granada', 'Córdoba'), ('Seville', 'Cádiz'), ('Valencia', 'Alicante'), ('Barcelona', 'Zaragoza'), ('Madrid', 'San Sebastián')]
Note: in dfs_search to show the traversal, I used in_edges(), not edges(), to show first the deepest path, and then the rest of the paths.

2.Result for BFS traversal from the starting point Bilbao:
[('Bilbao', 'Madrid'), ('Bilbao', 'Valencia'), ('Bilbao', 'San Sebastián'), ('Madrid', 'Barcelona'), ('Madrid', 'Seville'), 
('Madrid', 'Zaragoza'), ('Madrid', 'Córdoba'), ('Madrid', 'Granada'), ('Valencia', 'Alicante'), ('Seville', 'Málaga'), ('Seville', 'Cádiz')]

3. DFS search goes from the starting node (Bilbao) and goes as deeply as possible into the graph, which is why we have a traversal from Bilbao to Madrid, then to Barcelona, then to Valencia, and so on
until the "deepest" node Cadiz. Then it goes to the rest of unvisited nodes from "bottom" towards the starting point Bilbao (which is why we have Valencia-Alicante, then going up to
Barcelona-Zaragoza, and then up again to Madrid-SanSebastian).

4. BFS search visits first every neighbor of the starting node (we have Bilbao-Madrid, Bilbao-Valencia, Bilbao-SanSebastian), then it goes to the first visited neighbor (Madrid)
and visits every neighbor of Madrid. Then it visits every unvisited neighbor of the second visited neighbor of Bilbao (Valencia), until it visits all neighbours of the neighbours of Bilbao.
Then it goes one layer deeper, and visits unvisited neighbours of the neighbours of Madrid, then Valencia, etc... until it visits all nodes of the graph. 
