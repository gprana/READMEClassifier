Every script uses a trap on RETURN.

##### Llist

The double linked list gets a controlling associative array variable with the keys `lname[type]`, `lname[nodes]` and `lname[id]` as well as a second index array variable `lname_idx`, which indexes all nodes in the right order. Any node of the list will get its own associative array variable with the following keys: `lname_$((lname[id] + 1))=([prev]= [next]= [data]=)`. Of course, `lname_idx` isn't necessary. But iterating over the list is still slower.

```
set         lname [element ...]
unset       lname

insert      lname index [element ...]
append      lname [element ...]
replace     lname first last [element ...]

index       lname [index]
range       lname [-r] first last

length      lname [-t]

traverse    lname [-r] index
```

##### Queue

One associative array variable will be used. Its keys are `qname[type]`, `qname[first]` and `qname[last]`. In the case of pushing many elements to the queue, an additional indexed array variable `qname_idx` would be a good idea.

```
set         qname
pushl       qname [element]
pushr       qname [element]
popl        qname [element]
popr        qname [element]
```
