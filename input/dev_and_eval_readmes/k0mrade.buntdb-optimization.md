# buntdb-optimization
search optimal key:value structure for buntdb

IndexString improvement

IndexString time is reduced from 32.485058468s to 26.732144865s. 
The index is based on 1628953 rows. 

Before commit 823e2ea1467b2a65f30f8f8469f00c7c29317dd3

bash-3.2$ go run bunt-optimization.go                                                                                                                                             
Reading Bunt database --> 10.118220838s                                                                                                                                           
String index AD000007 creation time --> 32.485058468s                                                                                                                             
String index AD000008 creation time --> 4.319463065s                                                                                                                              
Indexes list --> [AD000007 AD000008]                                                                                                                                              
Reading 1843230 rows from BuntDB was --> 1.968400782s                                                                                                                             
Reading 1628953 rows from index AD000007 was --> 1.270601993s                                                                                                                     
Reading 214277 rows from index AD000008 was --> 141.407204ms 

After commit 823e2ea1467b2a65f30f8f8469f00c7c29317dd3

bash-3.2$ go run bunt-optimization.go                                                                                                                                                 
Reading Bunt database --> 8.927277245s                                                                                                                                            
String index AD000007 creation time --> 26.732144865s                                                                                                                             
String index AD000008 creation time --> 4.213542682s                                                                                                                              
Indexes list --> [AD000007 AD000008]                                                                                                                                              
Reading 1843230 rows from BuntDB was --> 1.68400849s                                                                                                                              
Reading 1628953 rows from index AD000007 was --> 1.343550111s                                                                                                                     
Reading 214277 rows from index AD000008 was --> 217.864232ms   


