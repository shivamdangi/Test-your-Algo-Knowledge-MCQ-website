import streamlit as st

# Define questions and answers with options
questions = {
    "Recover the BST": [
        {"question": "What is the primary purpose of recovering a Binary Search Tree (BST)?",
         "options": ["To optimize its search operation",
                     "To ensure its structural integrity after modifications",
                     "To reduce its memory consumption",
                     "To increase its traversal speed"],
         "correct_answer": " To ensure its structural integrity after modifications"},
        {"question": "Which of the following operations can lead to the need for recovering a BST?",
         "options": ["Insertion", "Deletion", "Searching", "Traversal"],
         "correct_answer": " Deletion"},
        {"question": "In a Binary Search Tree, what property must be maintained after a node deletion?",
         "options": ["In-order traversal property", "Pre-order traversal property",
                     "Post-order traversal property", "Binary search property"],
         "correct_answer": " Binary search property"},
        {"question": "Which of the following algorithms can be used for recovering a BST after a deletion?",
         "options": ["Breadth-first search (BFS)", "Depth-first search (DFS)",
                     "In-order traversal", "Dijkstra's algorithm"],
         "correct_answer": " In-order traversal"},
        {"question": "What does the in-order traversal of a BST produce?",
         "options": ["Nodes in sorted order", "Nodes in reverse sorted order",
                     "Nodes in random order", "Nodes in the order they were inserted"],
         "correct_answer": " Nodes in sorted order"},
        {"question": "When recovering a BST after a deletion, which of the following cases is the simplest to handle?",
         "options": ["Node with no children", "Node with one child",
                     "Node with two children", "Node with three children"],
         "correct_answer": " Node with no children"},
        {"question": "Which of the following is NOT a step in recovering a BST after a deletion?",
         "options": ["Finding the node to be deleted", "Deleting the node",
                     "Rebalancing the tree", "Reorganizing the tree to maintain the binary search property"],
         "correct_answer": " Rebalancing the tree"},
        {"question": "Which data structure is commonly used for tracking parent nodes during BST recovery?",
         "options": ["Queue", "Stack", "Linked list", "Array"],
         "correct_answer": " Stack"},
        {"question": "In the case of a node with two children being deleted from a BST, which node is typically chosen as its replacement?",
         "options": ["The node's left child", "The node's right child",
                     "The node's parent", "A random node from the tree"],
         "correct_answer": " The node's right child"},
        {"question": "After recovering a BST following a deletion, what operation should be performed to ensure the tree is balanced?",
         "options": ["Rotate the tree", "Reorder the nodes",
                     "Recalculate the heights of all nodes", "Perform a rebalancing operation like AVL or Red-Black tree rotations"],
         "correct_answer": "  Perform a rebalancing operation like AVL or Red-Black tree rotations"}
    ],
    "Views of tree": [
        {"question": "What is the view of a tree?",
         "options": ["The way the tree is displayed on the screen",
                     "The total number of nodes in the tree",
                     "The representation of the tree from a particular direction",
                     "The height of the tree"],
         "correct_answer": " The representation of the tree from a particular direction"},
        {"question": "Which of the following is NOT a type of tree view?",
         "options": ["Level order view", "Pre-order view", "In-order view", "Post-order view"],
         "correct_answer": " Pre-order view"},
        {"question": "What does the level order view of a tree display?",
         "options": ["Nodes at odd levels", "Nodes at even levels",
                     "Nodes at every level, from left to right", "Nodes at the root level only"],
         "correct_answer": " Nodes at every level, from left to right"},
        {"question": "Which view of a tree displays nodes as they are encountered during a depth-first traversal?",
         "options": ["In-order view", "Pre-order view", "Post-order view", "Level order view"],
         "correct_answer": " Pre-order view"},
        {"question": "In the post-order view of a binary tree, when is a node visited?",
         "options": ["Before visiting its left child", "After visiting its left child",
                     "Before visiting its right child", "After visiting its right child"],
         "correct_answer": "  After visiting its right child"},
        {"question": "Which view of a tree is also known as the breadth-first traversal?",
         "options": ["Pre-order view", "In-order view", "Level order view", "Post-order view"],
         "correct_answer": " Level order view"},
        {"question": "Which view of a binary tree is used in the expression tree evaluation?",
         "options": ["Pre-order view", "In-order view", "Post-order view", "Level order view"],
         "correct_answer": " In-order view"},
        {"question": "What is the main advantage of the level order view of a tree?",
         "options": ["It requires less memory", "It is faster than other views",
                     "It displays the structure of the tree clearly", "It is easier to implement"],
         "correct_answer": " It displays the structure of the tree clearly"},
        {"question": "Which view of a binary tree is used to create a copy of the tree?",
         "options": ["Pre-order view", "In-order view", "Post-order view", "Level order view"],
         "correct_answer": "a) Pre-order view"},
        {"question": "In a binary tree, which view provides nodes in non-decreasing order when the tree is a binary search tree (BST)?",
         "options": ["Pre-order view", "In-order view", "Post-order view", "Level order view"],
         "correct_answer": " In-order view"}
    ],
    "BFS": [
        {"question": "What is Breadth-First Search (BFS) primarily used for?",
         "options": ["Finding the shortest path in a weighted graph",
                     "Traversing and searching tree or graph data structures",
                     "Sorting elements in an array",
                     "Determining the longest path in a directed acyclic graph (DAG)"],
         "correct_answer": " Traversing and searching tree or graph data structures"},
        {"question": "In BFS, which data structure is typically used to store the vertices of the graph or tree?",
         "options": ["Stack", "Queue", "Priority queue", "Linked list"],
         "correct_answer": " Queue"},
        {"question": "What is the time complexity of BFS when applied to an adjacency matrix representation of a graph with V vertices and E edges?",
         "options": ["O(V)", "O(E)", "O(V + E)", "O(V log V)"],
         "correct_answer": " O(V + E)"},
        {"question": "In BFS, which vertices are explored first?",
         "options": ["Vertices with lower degree", "Vertices with higher degree",
                     "Vertices with the lowest value", "Vertices with the highest value"],
         "correct_answer": " Vertices with the lowest value"},
        {"question": "What is the order of traversal in BFS?",
         "options": ["Depth-first", "Pre-order", "Post-order", "Level-order"],
         "correct_answer": "  Level-order"},
        {"question": "In BFS, which traversal strategy is employed to visit neighboring vertices of a vertex?",
         "options": ["Depth-first traversal", "In-order traversal",
                     "Level-order traversal", "Post-order traversal"],
         "correct_answer": " Level-order traversal"},
        {"question": "Which of the following statements about BFS is true?",
         "options": ["BFS can be used to find the topological sorting of a graph.",
                     "BFS cannot handle graphs with cycles.",
                     "BFS is not optimal for finding the shortest path in an unweighted graph.",
                     "BFS explores vertices in the order they are discovered."],
         "correct_answer": "  BFS explores vertices in the order they are discovered."},
        {"question": "Which of the following is NOT a step in BFS?",
         "options": ["Enqueue the starting vertex", "Dequeue the starting vertex",
                     "Enqueue neighboring vertices", "Dequeue neighboring vertices"],
         "correct_answer": " Dequeue the starting vertex"},
        {"question": "In BFS, when should a visited vertex be enqueued?",
         "options": ["Before exploring its neighbors", "After exploring its neighbors",
                     "Before dequeueing its neighbors", "After dequeueing its neighbors"],
         "correct_answer": "a) Before exploring its neighbors"},
        {"question": "What is the space complexity of BFS?",
         "options": ["O(V)", "O(E)", "O(V + E)", "O(V log V)"],
         "correct_answer": "a) O(V)"}
    ],
    "DFS": [
        {"question": "What is Depth-First Search (DFS) primarily used for?",
         "options": ["Finding the shortest path in a weighted graph",
                     "Traversing and searching tree or graph data structures",
                     "Sorting elements in an array",
                     "Determining the longest path in a directed acyclic graph (DAG)"],
         "correct_answer": " Traversing and searching tree or graph data structures"},
        {"question": "Which data structure is typically used for implementing DFS?",
         "options": ["Queue", "Stack", "Priority queue", "Linked list"],
         "correct_answer": " Stack"},
        {"question": "What is the time complexity of DFS when applied to an adjacency list representation of a graph with V vertices and E edges?",
         "options": ["O(V)", "O(E)", "O(V + E)", "O(V log V)"],
         "correct_answer": " O(V + E)"},
        {"question": "In DFS, which traversal strategy is employed to explore neighboring vertices?",
         "options": ["Depth-first traversal", "In-order traversal",
                     "Level-order traversal", "Post-order traversal"],
         "correct_answer": "a) Depth-first traversal"},
        {"question": "What is the order of traversal in DFS?",
         "options": ["Depth-first", "Pre-order", "Post-order", "Level-order"],
         "correct_answer": "a) Depth-first"},
        {"question": "Which of the following statements about DFS is true?",
         "options": ["DFS always finds the shortest path in a graph.",
                     "DFS uses a FIFO strategy for exploring vertices.",
                     "DFS may result in a disconnected graph.",
                     "DFS explores vertices in the order they are discovered."],
         "correct_answer": " DFS may result in a disconnected graph."},
        {"question": "What is the main disadvantage of using recursion for implementing DFS?",
         "options": ["Recursion has higher space complexity compared to iterative methods.",
                     "Recursion is slower than iterative methods.",
                     "Recursion may lead to stack overflow for large graphs.",
                     "Recursion cannot handle graphs with cycles."],
         "correct_answer": " Recursion may lead to stack overflow for large graphs."},
        {"question": "Which of the following is NOT a step in DFS?",
         "options": ["Enqueue the starting vertex", "Process the current vertex",
                     "Recursively explore neighboring vertices", "Backtrack to the previous vertex"],
         "correct_answer": "a) Enqueue the starting vertex"},
        {"question": "In DFS, when should a visited vertex be marked?",
         "options": ["Before exploring its neighbors", "After exploring its neighbors",
                     "Before recursively calling DFS on its neighbors", "After recursively calling DFS on its neighbors"],
         "correct_answer": " After exploring its neighbors"},
        {"question": "What is the space complexity of DFS?",
         "options": ["O(V)", "O(E)", "O(V + E)", "O(V log V)"],
         "correct_answer": "a) O(V)"}
    ],
    "Binomial heap": [
        {"question": "What is a binomial tree?",
         "options": ["A tree where each node has at most two children",
                     "A tree where each node has exactly two children",
                     "A tree with a specific ordering of nodes",
                     "A tree used in binary search algorithms"],
         "correct_answer": " A tree where each node has exactly two children"},
        {"question": "Which operation is NOT supported efficiently by a binomial heap?",
         "options": ["Insertion", "Deletion", "Union", "Search"],
         "correct_answer": "  Search"},
        {"question": "In a binomial heap, what is the time complexity of inserting a new element?",
         "options": ["O(log n)", "O(n)", "O(log^2 n)", "O(1)"],
         "correct_answer": "a) O(log n)"},
        {"question": "What is the maximum height of a binomial tree with n nodes?",
         "options": ["n", "2n", "log_2 n", "log_2 (n+1)"],
         "correct_answer": "  log_2 (n+1)"},
        {"question": "Which of the following is a property of a binomial tree of order k?",
         "options": ["It has k children", "It has 2^k nodes",
                     "It has k+1 nodes", "It has 2^(k+1) - 1 nodes"],
         "correct_answer": " It has 2^k nodes"},
        {"question": "What operation is typically used to merge two binomial heaps?",
         "options": ["Union", "Intersection", "Difference", "Addition"],
         "correct_answer": "a) Union"},
        {"question": "Which of the following statements about binomial heaps is true?",
         "options": ["They are always balanced binary trees",
                     "They support constant time insertion and deletion",
                     "They are typically implemented using arrays",
                     "They have a worst-case time complexity of O(log n) for most operations"],
         "correct_answer": "  They have a worst-case time complexity of O(log n) for most operations"},
        {"question": "In a binomial heap, what is the purpose of the 'merge' operation?",
         "options": ["Combining two trees of the same order into one tree of the next order",
                     "Splitting a tree into smaller trees",
                     "Finding the minimum element in the heap",
                     "Deleting an element from the heap"],
         "correct_answer": "a) Combining two trees of the same order into one tree of the next order"},
        {"question": "Which of the following is NOT a common application of binomial heaps?",
         "options": ["Priority queue", "Sorting algorithms",
                     "Dijkstra's shortest path algorithm", "Prim's minimum spanning tree algorithm"],
         "correct_answer": " Sorting algorithms"},
        {"question": "What is the advantage of using a binomial heap over a binary heap?",
         "options": ["Binomial heaps have better worst-case time complexity for most operations",
                     "Binary heaps are more space efficient",
                     "Binomial heaps support more operations",
                     "Binary heaps are easier to implement"],
         "correct_answer": "a) Binomial heaps have better worst-case time complexity for most operations"}
    ],
    "Winner tree": [
        {"question": "What is the purpose of a winner tree?",
         "options": ["To store elements in a sorted order",
                     "To efficiently find the maximum (or minimum) element among a set of elements",
                     "To balance binary search trees",
                     "To implement priority queues"],
         "correct_answer": " To efficiently find the maximum (or minimum) element among a set of elements"},
        {"question": "In a winner tree, what do the leaves represent?",
         "options": ["Internal nodes", "The maximum element", "The elements themselves", "The minimum element"],
         "correct_answer": " The elements themselves"},
        {"question": "How are winner trees commonly used in algorithms?",
         "options": ["For graph traversal", "For heap sort",
                     "For tournament-style algorithms", "For binary search"],
         "correct_answer": " For tournament-style algorithms"},
        {"question": "Which node of a winner tree contains the overall winner?",
         "options": ["Root node", "Leaf nodes", "Internal nodes", "None of the above"],
         "correct_answer": "a) Root node"},
        {"question": "What operation is performed to construct a winner tree?",
         "options": ["Merge", "Compare", "Split", "Rotate"],
         "correct_answer": " Compare"},
        {"question": "Which of the following is NOT a step in using a winner tree to find the maximum element?",
         "options": ["Initialize the winner tree", "Insert elements in random order",
                     "Construct the winner tree", "Access the root node"],
         "correct_answer": " Insert elements in random order"},
        {"question": "What type of elements can be compared using a winner tree?",
         "options": ["Numbers only", "Strings only",
                     "Any comparable elements", "Only elements of the same type"],
         "correct_answer": " Any comparable elements"},
        {"question": "How does a winner tree compare elements?",
         "options": ["Using hashing", "By iterating through all elements",
                     "By comparing pairs of elements recursively", "By performing binary search"],
         "correct_answer": " By comparing pairs of elements recursively"},
        {"question": "Which data structure is NOT commonly implemented using winner trees?",
         "options": ["Priority queue", "Heap", "Hash table", "Tournament bracket"],
         "correct_answer": " Hash table"},
        {"question": "In a winner tree with n elements, how many comparisons are needed to find the maximum element?",
         "options": ["n", "log n", "2n - 1", "n^2"],
         "correct_answer": " log n"}
    ],
    "Bellman Ford Algorithm": [
        {
            "question": "What is the Bellman-Ford algorithm used for?",
            "options": [
                "Finding the shortest path in a weighted directed graph with negative edge weights",
                "Sorting elements in an array",
                "Implementing a priority queue",
                "Searching for an element in a binary search tree"
            ],
            "correct_answer": "a) Finding the shortest path in a weighted directed graph with negative edge weights"
        },
        {
            "question": "Which data structure is commonly used to represent graphs in the Bellman-Ford algorithm?",
            "options": [
                "Arrays",
                "Linked lists",
                "Hash tables",
                "Adjacency matrices or adjacency lists"
            ],
            "correct_answer": "d) Adjacency matrices or adjacency lists"
        },
        {
            "question": "What is the time complexity of the Bellman-Ford algorithm?",
            "options": [
                "O(V)",
                "O(V log V)",
                "O(V + E)",
                "O(V^2)"
            ],
            "correct_answer": "c) O(V + E)"
        },
        {
            "question": "In the context of the Bellman-Ford algorithm, what does 'V' represent?",
            "options": [
                "The number of vertices in the graph",
                "The number of edges in the graph",
                "The maximum possible weight of an edge",
                "The source vertex"
            ],
            "correct_answer": "a) The number of vertices in the graph"
        },
        {
            "question": "What does the Bellman-Ford algorithm initialize the shortest distance to each vertex with?",
            "options": [
                "Positive infinity",
                "Negative infinity",
                "Zero",
                "The weight of the source vertex to itself"
            ],
            "correct_answer": "a) Positive infinity"
        },
        {
            "question": "What is the purpose of the relaxation step in the Bellman-Ford algorithm?",
            "options": [
                "To initialize the shortest distances",
                "To update the shortest distances if a shorter path is found",
                "To remove edges with negative weights",
                "To reverse the direction of edges in the graph"
            ],
            "correct_answer": "b) To update the shortest distances if a shorter path is found"
        },
        {
            "question": "What does a negative cycle in a graph indicate in the context of the Bellman-Ford algorithm?",
            "options": [
                "The graph has no shortest paths",
                "The graph contains edges with negative weights",
                "The graph has multiple shortest paths between some pairs of vertices",
                "The graph has a cycle whose total weight is negative"
            ],
            "correct_answer": "d) The graph has a cycle whose total weight is negative"
        },
        {
            "question": "Which step in the Bellman-Ford algorithm detects negative cycles?",
            "options": [
                "Initialization",
                "Relaxation",
                "Shortest path determination",
                "Negative cycle detection"
            ],
            "correct_answer": "d) Negative cycle detection"
        },
        {
            "question": "When does the Bellman-Ford algorithm terminate?",
            "options": [
                "After a fixed number of iterations",
                "When all vertices have been visited",
                "When no more relaxation can be performed",
                "When a negative cycle is detected"
            ],
            "correct_answer": "c) When no more relaxation can be performed"
        },
        {
            "question": "What does the Bellman-Ford algorithm return if a negative cycle is detected?",
            "options": [
                "The shortest paths to all vertices",
                "The shortest path from the source vertex to a specific target vertex",
                "An error indicating the presence of a negative cycle",
                "The length of the shortest path"
            ],
            "correct_answer": "c) An error indicating the presence of a negative cycle"
        }
    ],
    "Dijkstra's Algorithm": [
        {
            "question": "What is Dijkstra's algorithm primarily used for?",
            "options": [
                "Finding the longest path in a graph",
                "Finding the shortest path in a graph with non-negative edge weights",
                "Sorting elements in an array",
                "Detecting cycles in a graph"
            ],
            "correct_answer": "b) Finding the shortest path in a graph with non-negative edge weights"
        },
        {
            "question": "Which data structure is commonly used in Dijkstra's algorithm?",
            "options": [
                "Queue",
                "Stack",
                "Heap",
                "Linked list"
            ],
            "correct_answer": "c) Heap"
        },
        {
            "question": "What is the time complexity of Dijkstra's algorithm?",
            "options": [
                "O(V)",
                "O(V log V)",
                "O(V + E)",
                "O(V^2)"
            ],
            "correct_answer": "c) O(V + E)"
        },
        {
            "question": "In Dijkstra's algorithm, how are the vertices processed?",
            "options": [
                "In a depth-first manner",
                "In a breadth-first manner",
                "Based on their distance from the source vertex",
                "Randomly"
            ],
            "correct_answer": "c) Based on their distance from the source vertex"
        },
        {
            "question": "What is the purpose of the priority queue in Dijkstra's algorithm?",
            "options": [
                "To maintain the order of vertices based on their IDs",
                "To maintain the order of vertices based on their distances from the source",
                "To store the vertices in a sorted array",
                "To store the vertices in a linked list"
            ],
            "correct_answer": "b) To maintain the order of vertices based on their distances from the source"
        },
        {
            "question": "What does Dijkstra's algorithm initialize the shortest distance to each vertex with?",
            "options": [
                "Positive infinity",
                "Negative infinity",
                "Zero",
                "The weight of the source vertex to itself"
            ],
            "correct_answer": "a) Positive infinity"
        },
        {
            "question": "What is the relaxation step in Dijkstra's algorithm?",
            "options": [
                "A step to initialize the shortest distances",
                "A step to update the shortest distances if a shorter path is found",
                "A step to remove edges with negative weights",
                "A step to reverse the direction of edges in the graph"
            ],
            "correct_answer": "b) A step to update the shortest distances if a shorter path is found"
        },
        {
            "question": "In Dijkstra's algorithm, when is a vertex removed from the priority queue?",
            "options": [
                "When it has been visited once",
                "When it has been visited twice",
                "When its distance from the source is updated",
                "When it is added to the priority queue"
            ],
            "correct_answer": "c) When its distance from the source is updated"
        },
        {
            "question": "When does Dijkstra's algorithm terminate?",
            "options": [
                "When all vertices have been visited",
                "When the priority queue becomes empty",
                "When a negative cycle is detected",
                "When a certain number of iterations is reached"
            ],
            "correct_answer": "b) When the priority queue becomes empty"
        },
        {
            "question": "What does Dijkstra's algorithm return as output?",
            "options": [
                "The shortest paths to all vertices",
                "The shortest path from the source vertex to a specific target vertex",
                "An error if a negative cycle is detected",
                "The vertices visited during the traversal"
            ],
            "correct_answer": "a) The shortest paths to all vertices"
        }
    ],
    "Topological Sort": [
        {
            "question": "What is topological sorting used for?",
            "options": [
                "Finding shortest paths in a graph",
                "Detecting cycles in a graph",
                "Ordering tasks with dependencies",
                "Generating minimum spanning trees"
            ],
            "correct_answer": "c) Ordering tasks with dependencies"
        },
        {
            "question": "Which of the following data structures is commonly used to implement topological sorting?",
            "options": [
                "Queue",
                "Stack",
                "Array",
                "Heap"
            ],
            "correct_answer": "b) Stack"
        },
        {
            "question": "In a directed acyclic graph (DAG), topological sorting results in:",
            "options": [
                "A linear ordering of vertices",
                "A minimum spanning tree",
                "A cyclic dependency graph",
                "A binary search tree"
            ],
            "correct_answer": "a) A linear ordering of vertices"
        },
        {
            "question": "Which algorithm is commonly used to perform topological sorting?",
            "options": [
                "Breadth-first search (BFS)",
                "Depth-first search (DFS)",
                "Dijkstra's algorithm",
                "Prim's algorithm"
            ],
            "correct_answer": "b) Depth-first search (DFS)"
        },
        {
            "question": "In topological sorting, vertices with no incoming edges are processed:",
            "options": [
                "First",
                "Last",
                "Randomly",
                "In any order"
            ],
            "correct_answer": "a) First"
        },
        {
            "question": "If a graph has a cycle, what happens during topological sorting?",
            "options": [
                "The algorithm fails",
                "The cycle is ignored",
                "The cycle is broken",
                "The algorithm continues indefinitely"
            ],
            "correct_answer": "a) The algorithm fails"
        },
        {
            "question": "Topological sorting can be applied to which type of graphs?",
            "options": [
                "Directed graphs",
                "Undirected graphs",
                "Weighted graphs",
                "Bipartite graphs"
            ],
            "correct_answer": "a) Directed graphs"
        },
        {
            "question": "Which of the following statements is true about topological sorting?",
            "options": [
                "It always produces a unique ordering of vertices.",
                "It can only be applied to graphs with a single source and sink.",
                "It can have multiple valid orderings for a given graph.",
                "It has a time complexity of O(nlogn)."
            ],
            "correct_answer": "c) It can have multiple valid orderings for a given graph."
        },
        {
            "question": "In a directed acyclic graph (DAG), if there are multiple vertices with no incoming edges, which one is processed first during topological sorting?",
            "options": [
                "The vertex with the highest index",
                "The vertex with the lowest index",
                "Any of the vertices with no incoming edges",
                "None of the above"
            ],
            "correct_answer": "c) Any of the vertices with no incoming edges"
        },
        {
            "question": "In a directed acyclic graph (DAG) with vertices a, b, c, d, and e and edges ab, bc, cd, and de, what would be the topological sorting order?",
            "options": [
                "a, b, c, d, e",
                "e, d, c, b, a",
                "a, e, b, c, d",
                "a, b, c, e, d"
            ],
            "correct_answer": "d) a, b, c, e, d"
        }
    ],
    "Vertical Order Traversal": [
        {
            "question": "What does vertical order traversal of a binary tree involve?",
            "options": [
                "Traversing the tree level by level",
                "Visiting nodes from left to right",
                "Exploring nodes from top to bottom",
                "Grouping nodes based on their horizontal distance from the root"
            ],
            "correct_answer": "d) Grouping nodes based on their horizontal distance from the root"
        },
        {
            "question": "Which data structure is commonly used to perform vertical order traversal?",
            "options": [
                "Array",
                "Queue",
                "Stack",
                "Linked list"
            ],
            "correct_answer": "b) Queue"
        },
        {
            "question": "In vertical order traversal, nodes at the same horizontal distance are visited in which order?",
            "options": [
                "Random",
                "Pre-order",
                "Level-order",
                "Post-order"
            ],
            "correct_answer": "c) Level-order"
        },
        {
            "question": "What is the time complexity of vertical order traversal in a binary tree with n nodes?",
            "options": [
                "O(n)",
                "O(n log n)",
                "O(n^2)",
                "O(2^n)"
            ],
            "correct_answer": "a) O(n)"
        },
        {
            "question": "Which traversal technique is typically used to implement vertical order traversal?",
            "options": [
                "Depth-first traversal",
                "Breadth-first traversal",
                "In-order traversal",
                "Pre-order traversal"
            ],
            "correct_answer": "b) Breadth-first traversal"
        },
        {
            "question": "In vertical order traversal, which node is visited first at a particular horizontal distance?",
            "options": [
                "Left child",
                "Right child",
                "Root node",
                "Parent node"
            ],
            "correct_answer": "c) Root node"
        },
        {
            "question": "If two nodes in a binary tree have the same horizontal distance from the root, which one is visited first in vertical order traversal?",
            "options": [
                "Left node",
                "Right node",
                "It depends on the tree structure",
                "Both nodes are visited simultaneously"
            ],
            "correct_answer": "a) Left node"
        },
        {
            "question": "Which of the following statements is true about vertical order traversal?",
            "options": [
                "It only works for balanced binary trees",
                "It doesn't guarantee the nodes will be visited in sorted order",
                "It preserves the original tree structure",
                "It cannot handle binary trees with more than two children per node"
            ],
            "correct_answer": "b) It doesn't guarantee the nodes will be visited in sorted order"
        },
        {
            "question": "What is the space complexity of vertical order traversal?",
            "options": [
                "O(n)",
                "O(log n)",
                "O(1)",
                "O(n^2)"
            ],
            "correct_answer": "a) O(n)"
        },
        {
            "question": "Which of the following scenarios might require additional techniques to handle during vertical order traversal?",
            "options": [
                "Binary tree with only one child per node",
                "Binary tree with multiple nodes at the same horizontal distance",
                "Binary tree with unbalanced branches",
                "Binary tree with a height less than two"
            ],
            "correct_answer": "b) Binary tree with multiple nodes at the same horizontal distance"
        }
    ]
}

def display_question(question_data):
    st.markdown(f"<u><b>{question_data['question']}</b></u>", unsafe_allow_html=True)
    selected_option = st.radio("Choose the correct option:", options=question_data["options"])
    return selected_option

def main():
    st.title("MCQ Quiz")
    topic = st.selectbox("Select Topic", list(questions.keys()))

    score = 0  # Initialize score

    for i, question_data in enumerate(questions[topic]):
        selected_option = display_question(question_data)
        correct_answer = question_data["correct_answer"]
        correct_option_letter = correct_answer.split(")")[0].strip()

        # Generate a unique key for the "Submit" button
        submit_button_key = f"submit_button_{topic}_{i}"

        if st.button("Submit", key=submit_button_key):
            selected_option_letter = selected_option.split(")")[0].strip()
            if selected_option_letter == correct_option_letter:
                score += 1  # Increment score for correct answer
                st.write("<span style='color:green'>Correct!</span>", unsafe_allow_html=True)
            else:
                st.write("<span style='color:red'>Incorrect! The correct answer is:</span> " + correct_answer, unsafe_allow_html=True)

    

if __name__ == "__main__":
    main()