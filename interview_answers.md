# Interview responses

1. Hashing functions

`hash functions are used to create an index. This is used to map out data with a fixed-sized range of index values in a hash table.`

2. Collision resolution

`collisions occur when a hash function returns an index value that is already used in the hash table. In order to resolve this we can use a linked list to add multiple values`

3. Performance of basic hash table operations

`a hash tables performance is O(1) since it does not need to loop through it. It uses the key to go directly and find the value`

4. Load factor

`the load factor in a hash table is calculated by finding the quotient of the number of 'buckets' or spaces used by the total number of buckets. This is used to determine when we should resize or rehash the table to continue fitting more data and the hash function to continue giving correct indices`

5. Automatic resizing

`Automatic resizing is done when the load factor is greater than .7 as a good rule of thumb. This is done as result of more data being entered than the hash table currently has space for.`

6. Various use cases for hash tables

`A hash table is used to create the python dictionary data structure. A hash table can be used to create the functionality of a set. It is very common to use it as cache memory to improve performance`
