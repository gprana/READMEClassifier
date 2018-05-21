# Crash course in collections with Java 8

All exercises can be done in `main` method of [CollectionsExercises](CollectionsExercises.java) class.
## Lambda Expressions
### Example
Writing down elements of given `beerNames` list:
```java
beerNames.forEach(s -> System.out.println(s));
```
### Example
Sorting given list in aphabet order:
```java
beerNames.sort((String a, String b) -> {return a.compareTo(b);});
```
### Explanation
Functional Inrerface is interface with exaclty one abstract method. It can be annotated with `@FuctionalInterface`. In Java 8 there are built in functional interfaces i.e. `Comparator` (with `compare` abstract method). When lambda is implementation of abstract method of functional interface, instance of this functional interface can be created as follows.
#### Example
```java
Comparator<String> comparator = (String a, String b) -> {return a.compareTo(b);};

beerNames.sort(comparator);
```
### Syntax
General form of lambda expression is 
```java
(parameters) -> { statements;}  // (String a, String b) -> {return a.compareTo(b);}
```
When there is only one expresion, it can be simplified as follows (`return` should me ommitted):
```java
(parameters) -> expression      // (String a, String b) -> a.compareTo(b)
```
When type declaration can be ommited, it can be simplified as follows:
```java
(parameters) -> expression      // (a, b) -> a.compareTo(b)
```
When there is only one parameter and there is no need to declare type, it can be simplified as follows:
```java
parameter -> expression         // (String s) -> System.out.printout(s)
                                // to
                                // s -> System.out.println(s)
```
### Exercise 1
Simplify lambda in following code snippet.
```jave
Collections.sort(beerNames, (String a, String b) -> {return a.compareTo(b);} );
```
#### Solution
<details>
<summary>Click to show</summary>

Lambda can be simplified as follows:
```java
(String a, String b) -> a.compareTo(b)
```
or
```java
(a, b) -> a.compareTo(b)
```
</details>

### Example
Consider following code snippet.
```jave
Collections.sort(beerNames, (a, b) -> a.compareTo(b));
```
Since Java 8, `List` interface has `sort` method which takes one parameter - instance of `Comparator`. `Collections.sort` can be replaced as follows:
```java
beerNames.sort((a, b) -> a.compareTo(b));
```
### Exercise 2
Refactor following code to Java 8 level.
```jave
Collections.sort(beers, new Comparator<Beer>() {
    @Override
    public int compare(Beer a, Beer b) {
        return a.getBottleVolume() - b.getBottleVolume();
    }
});
```
#### Solution
<details>
<summary>Click to show</summary>

Replace `Collections.sort` with `List.sort` and replace anonymous class with lambda:
```java
beers.sort((a, b) -> a.getBottleVolume() - b.getBottleVolume());
```
</details>

## Method References
Lambda expressions can be replaced with method references. Method reference has following form:
```java
ClassName :: methodName
```
#### Rule of thumb for replacing lambda with reference method:
```java
lambda form                      |  reference method form
-------------------------------------------------------------------------------------------------
p -> ClassName.methodName(p)     |  ClassName::methodName
p -> new ClassName(p)            |  ClassName::new
p -> p.methodName()              |  ClassName::methodName // where ClassName is class of object p
(p, q) -> p.methodName(q)        |  ClassName::methodName // where ClassName is class of object p
```
Examples (respectivly):
```java
lambda                           |  reference method
-------------------------------------------------------------------------------------------------
p -> System.out.println(p)       |  System.out::println
p -> new HashSet<>(p)            |  HashSet::new
p -> p.getName()                 |  Beer::getName 
(p, q) -> p.compareTo(q)         |  String::compareTo
```
### Exercise 3
Replace lambda expression with method reference.
```java
beerNames.forEach(s -> System.out.println(s));
```
#### Solution
<details>
<summary>Click to show</summary>

```java
beerNames.forEach(System.out::println);
```
</details>

### Exercise 4
Replace lambda expression with method reference.
```java
beerNames.sort((a, b) -> a.compareTo(b));
```
#### Solution
<details>
<summary>Click to show</summary>

```java
beerNames.sort(String::compareTo);
```
</details>

### Exercise 5
Replace lambda expressions with method references.
```java
beers.stream()
        .map(b -> b.getName())
        .forEach(b -> System.out.println(b));
```
#### Solution
<details>
<summary>Click to show</summary>

```java
beers.stream()
        .map(Beer::getName)
        .forEach(System.out::println);
```
</details>

### Exercise 6
Replace lambda expressions with method reference.
```java
beers.stream()
        .map(b -> b.getHops())
        .map(b -> new HashSet<>(b))
        .forEach(b -> System.out.println(b));
```
#### Solution
<details>
<summary>Click to show</summary>

```java
beers.stream()
        .map(Beer::getHops)
        .map(HashSet::new)
        .forEach(System.out::println);
```
</details>

## Streams
Stream (`java.util.Stream`) is a sequence of elements supporting operations. There are two kinds of stream operations:
- intermediate (returns Stream) i.e.: `filter`
- terminal  (returns other type) i.e.: `forEach`

Operations on stream don't modify source of stream. Stream operations form stream pipelines.

## Streams: filter
### Example
Writing down beers that have more than 5.0% alcohol in volume:
```java
beers.stream()
        .filter(b -> b.getAlcoholByValue() > 5.0)
        .forEach(System.out::println);
```
#### Explanation
`Predicate` is functional interface which is boolean-valued function of one argument. 
Operation `filter` takes instance of `Predicate` as argument and reduces stream to elements for which `Predicate` return `true`. In above example predicate is lambda `b -> b.getAlcoholByValue() > 5.0`. `filter` is intermediate operation (as it returns stream).
### Exercise 7
Write down beers containg Cascade hop and not containg Amarillo hop.
#### Solution
<details>
<summary>Click to show</summary>

```java
beers.stream()
        .filter(b -> b.getHops().contains(HOP_CASCADE))
        .filter(b -> !b.getHops().contains(HOP_AMARILLO))
        .forEach(System.out::println);
```
</details>

## Streams: map
### Example
Writing down names of beers from given list.
```java
beers.stream()
        .map(b -> b.getName())
        .forEach(System.out::println);
```
#### Explanation
Operation `map` is intermediate operation (returns stream) which takes instance of `Function` as argument. It transforms (maps) each element of stream to another according to passed `Function`. `Function` is functonal interface.
### Exercise 8
Write down names of beers containg Cascade hop.
#### Solution
<details>
<summary>Click to show</summary>

```java
beers.stream()
        .filter(b -> b.getHops().contains(HOP_CASCADE))
        .map(b -> b.getName() )
        .forEach(System.out::println);
```
</details>

## Streams: sorted
Elements of stream can be sorted with `sorted` method. It takes instance of `Comparator` as argument. When `sorted` is called whitout argument, stream elements are sorted with natural order. `sorted` is intermediate operation.
### Exercise 9
Write down beers from given list ordered by bottle volume.
#### Solution
<details>
<summary>Click to show</summary>

```java
beers.stream()
        .sorted((a, b) -> (a.getBottleVolume() - b.getBottleVolume()))
        .forEach(System.out::println);
```
</details>

### Exercise 10
Write down names of beers in alphabetical (natural) order.
#### Solution
<details>
<summary>Click to show</summary>

```java
beers.stream()
        .map(Beer::getName)
        .sorted()
        .forEach(System.out::println);
```
</details>

## Streams: collect
Stream elements can be accumulated into collection with `collect` method (i.e. `collect(Collectors.toList())`, `Collectors.toCollection(toSet())`).
### Exercise 11
Create a list of beer names.
#### Solution
```java
beerNames = beers.stream()
        .map(b -> b.getName())
        .collect(Collectors.toList());
```
### Exercise 12
Create a list of beers that have more than 5.0% alcohol in volume.
#### Solution
<details>
<summary>Click to show</summary>

```java
List strongBeers = beers.stream()
        .filter(b -> b.alcoholByValue > 5.0)
        .collect(Collectors.toList());
```
</details>

### Example
Creating a map of beers with value of bottle volume as keys:
```java
Map beersByVolume = beers.stream()
        .collect(Collectors.groupingBy(b -> b.getBottleVolume()));

beersByVolume.forEach((k,v) -> System.out.println("key: " + k.toString() + " value: " + v.toString()));
```
Method `Collectors.groupingBy` is used to create map. It groups elements according to passed classification function.
### Exercise 13
Create a map of beer names with first letters as keys.
#### Solution
<details>
<summary>Click to show</summary>

```jave
Map beerIndex = beerNames.stream()
        .collect(Collectors.groupingBy(s -> s.charAt(0)));

beerIndex.forEach((k,v) -> System.out.println("key: " + k.toString() + " value: " + v.toString()));
```
</details>

### Exercise 14 (summing up: filter, map, sorted, collect)
Create a sorted list of beer names containing Cascade hop.
#### Solution
<details>
<summary>Click to show</summary>

```java
List<String> cascadeBeers = beers.stream()
        .filter(b -> b.getHops().contains(HOP_CASCADE))
        .map(Beer::getName)
        .sorted()
        .collect(Collectors.toList());
```
</details>

## Streams: other terminating methods
### Example
Printing sum of bottle volumes of beers from given list:
```java
int volumeSum = beers.stream()
          .mapToInt((beer) -> beer.getBottleVolume())
          .sum();

System.out.println(volumeSum);
```
### Example
Printing maximum bottle volume:
```java
OptionalInt maxVolume = beers.stream()
       .mapToInt((beer) -> beer.getBottleVolume())
       .max();
        
maxVolume.ifPresent(System.out::println);                
```
#### Explanation
Operation `max()` returns `OptionalInt` object. Class `Optional` (along with `OptionalInt` and `OptionalDouble`) is introduced to Java 8. It is container which can contain or not contain value. It protects against `NullPointerException` (no need to write `if (maxVolume != null)` checks). 
### Example
Print average bottle volume.
#### Solution 
```java
OptionalDouble averageVolume = beers.stream()
        .mapToInt((beer) -> beer.getBottleVolume())
        .average();

averageVolume.ifPresent(System.out::println);
```
### Exercise 15
Print average alcohol of beers:
- containing Cascade hop 
- with bottles volume bigger than 500 ml

#### Solution
<details>
<summary>Click to show</summary>

```java
OptionalDouble averageAlcohol = beers.stream()
        .filter(b -> b.getHops().contains(HOP_CASCADE))
        .filter(b -> b.getBottleVolume() > 500)
        .mapToDouble(b -> b.getAlcoholByValue())
        .average();

averageAlcohol.ifPresent(System.out::println);
```
</details>

## References
- Lambda Expressions (The Java Tutorials): https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html
- Java 8 Tutorial: http://winterbe.com/posts/2014/03/16/java-8-tutorial/
- Java 8 Stream Tutorial: http://winterbe.com/posts/2014/07/31/java8-stream-tutorial-examples/
