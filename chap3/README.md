# Chapter 3

## 3.1 Asymptotic notation
(learn x in y minutes)[https://learnxinyminutes.com/docs/asymptotic-notation/]  
### What is Asymptotic Notations?
They are languages that allow us to analyze an algorithm's running time by identifying its behavior as the input size for the algorithm increases. This is also known as an algorithm's **growth rate**. 

### Types of Asymptotic Notation
Asymptotic notation is primarily used to describe the running times of algorithms. You can label an algorithm in different ways.Some examples that we might use are, best case, worst case, or equivalent case. The most common is to analyze an algorithm by its worst case. You typically don't evaluate by best case because those conditions aren't what you're planning for.

#### Types of functions, limits, and simplification
```
Logarithmic Function: log n
Linear Function: an + b
Quadratic Function: an^2 + bn + c
Polynomial Function: an^z + . . . + an^2 + a*n^1 + a*n^0, where z is some 
constant
Exponential Function: a^n, where a is some constant
```
The list starts at the slowest growing function and goes on to the fastest growing. 'n' is the input, and as n increases in those functions, the growing rate increases as well.  
For simplicity, we'll modify the table a bit...  
```
Logarithmic: log n
Linear: n
Quadratic: n^2
Polynomial: n^z, where z is some constant
Exponential: a^n, where a is some constant
```

#### Big-O 
Big-O is an Asymptotic Notation for the **worst case**, or ceiling of growth for a given function. It provides us with an asymptotic upper bound for the growth rate of runtime of an algorithm. Say f(n) is your algorithm runtime, and g(n) us an arbitrary time complexity you are trying to relate to your algorithm. f(n) is O(g(n)), if for some real constants c (c>0) and n<sub>0</sub>, f(n) <= c g(n) for every input size n (n>n<sub>0</sub>).

#### Big-Omega
Big-Omega is an Asymptotic Notation for the best case, or a floor growth rate for a given function. It provides an asymptotic lower bound for the growth rate of runtime of an algorithm.

