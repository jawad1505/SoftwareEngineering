# SoftwareEngineering
Repo for understanding and practicing Core concepts

# Core Concepts
* Big O
* Omega
* Theta
* Recursion
* Dynamic Programming
* Memory ( Stack vs Heap)
* Bit Manipulation



# Data Structures
* Linked List
* Arrays
* Trees
  * Binary Trees
  * Full Binary Trees
  * Perfect Binary Trees
  * Complete Binary Trees
  * Balanced Binary Trees
  * Binary Search Trees
* Tries
* Graphs
  * Undirected Graphs
  * Directed Graphs
  * Minimum Spanning Trees
  * Shortest Path
* Heaps
* Vectors/ArrayList
* Hashlist
  * Hash Collision
  * Sets

# Algorithms
* Fundamentals
  * Stack
  * Queue
  * Bag
  * Union Find
* Sorting 
  * Merge Sort
  * Quick Sort
  * Inserting Sort
  * Selection Sort
  * ShellSort
  * top-down MergeSort
  * bottom-up mergesort
  * Quick Sort
  * Quick Sort with 3 partitioning
  * Heap Priority Queue
  * Heap Sort
* Symbol Tables
  * Binary Search
  * Sequential Search
  * Binary Tree Search
  * Red-Black BST search
  * Hashing with separate chaining
  * Hashing with linear probing
* Graphs
  * DFS
  * BFS
  * Connected components
  * Reachibility
  * Topological Sort
  * Strong Components ( Kosaraju)
  * Minimum spanning Tree ( Prim)
  * Minimum spanning Tree (Kruskal)
  * Shortest Paths ( Dijkstra)
  * shortest Paths ( Bellman-Ford)
  * Shortest path in DAGs

* Greedy Algorthims
* K-Nearest Neighbours
* Parallel algorithms
* Epilogue
* Linear Programming
* Locality- sensitive hashing
* Bloom filters and HyperLog
* Map reduce
* The fourier Transform
* Inverted Indexes
* Diffie-Hellman Keyexchange



We can expand the phone book example to compare other kinds of operations and their running time. We will assume our phone book has businesses (the "Yellow Pages") which have unique names and people (the "White Pages") which may not have unique names. A phone number is assigned to at most one person or business. We will also assume that it takes constant time to flip to a specific page.

Here are the running times of some operations we might perform on the phone book, from fastest to slowest:

O(1) (in the worst case): Given the page that a business's name is on and the business name, find the phone number.

O(1) (in the average case): Given the page that a person's name is on and their name, find the phone number.

O(log n): Given a person's name, find the phone number by picking a random point about halfway through the part of the book you haven't searched yet, then checking to see whether the person's name is at that point. Then repeat the process about halfway through the part of the book where the person's name lies. (This is a binary search for a person's name.)

O(n): Find all people whose phone numbers contain the digit "5".

O(n): Given a phone number, find the person or business with that number.

O(n log n): There was a mix-up at the printer's office, and our phone book had all its pages inserted in a random order. Fix the ordering so that it's correct by looking at the first name on each page and then putting that page in the appropriate spot in a new, empty phone book.

For the below examples, we're now at the printer's office. Phone books are waiting to be mailed to each resident or business, and there's a sticker on each phone book identifying where it should be mailed to. Every person or business gets one phone book.

O(n log n): We want to personalize the phone book, so we're going to find each person or business's name in their designated copy, then circle their name in the book and write a short thank-you note for their patronage.

O(n2): A mistake occurred at the office, and every entry in each of the phone books has an extra "0" at the end of the phone number. Take some white-out and remove each zero.

O(n · n!): We're ready to load the phonebooks onto the shipping dock. Unfortunately, the robot that was supposed to load the books has gone haywire: it's putting the books onto the truck in a random order! Even worse, it loads all the books onto the truck, then checks to see if they're in the right order, and if not, it unloads them and starts over. (This is the dreaded bogo sort.)

O(nn): You fix the robot so that it's loading things correctly. The next day, one of your co-workers plays a prank on you and wires the loading dock robot to the automated printing systems. Every time the robot goes to load an original book, the factory printer makes a duplicate run of all the phonebooks! Fortunately, the robot's bug-detection systems are sophisticated enough that the robot doesn't try printing even more copies when it encounters a duplicate book for loading, but it still has to load every original and duplicate book that's been printed.