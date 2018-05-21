Submission by Michael Raimi (raimi.michael@gmail.com)


##Implementation details

I decided to represent the graph as an adjacency list keyed by username which I assumed to be unique. 
This assumption was supported by the numerical suffixes on names such as 'Caroline-Kaiser-2'. The value
of the adjacency list is a tuple of the node's degree count and a set of neighbors the node shares an edge with. 
It's a set to prevent any bookkeeping issues in the event of records with the same target/actor pair.

The 60 second window is represented by a list (used essentially as a queue) of tuples of target, actor, datetime records.
It is always in order by timestamp and has linear insertion on out of order nodes but is O(1) otherwise.

NOTE: In the event that multiple records in the same 60 second window have the same target/actor pair
multiple records in the window are created with unique datetimes but no new edges are created, and
as a result no degree counts are modified. This has the same effect as updating the edge's timestamp.

Below are other data structures and counts used to support graph operations and modifications:

- There is a dictionary keeping track of how many instances of a certain degree exist in the graph
e.g. there are 6 nodes with degree 3.

- There is a list of integers that represents the current degree values in the graph 
e.g. there are nodes of degree 3, 6, 7, and so on. It's always sorted.

- There is a total node count used for sanity checking and to lookup the median

- There is a dictionary keeping count of how many times a unique target/actor
pair is received. The size of this data structure is linear in the number of edges and vertices
of the graph multiplied by some factor d, which represents the highest number of records made by a
single target/actor pair. In Big-O it would be O(d(V + E)). This implementation would be prohibitive in
the case where a few power users make tons of transactions. An alternative implementation to this would 
be to remove the old record from the window and insert the new one in the correct position. 
This would have linear processing cost in the size of records in the window but could 
reduce the memory footprint by a constant factor. This implementation would be somewhat prohibitive 
in the case of a window with many records all fitting within the 60 second constraint as an insertion

##Calculating the median
If we imagine all the possible degree values in a sorted list we could use the size of the
list to find the value(s) in the middle representing the median degree.
This code uses a similar approach by using the total node count, sorted degree keys, and the degree count
dictionary to find the median. In short we iterate through the keys, using each one to key into the dictionary
to find the degree where the median lies. It runs in time linear in the size of the degree key list
which in the big dataset of 1800 was of size < 20.

Thanks for taking the time to consider me for the fellowship!





