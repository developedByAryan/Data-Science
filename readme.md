#Python Notes



**Primitive Data Types**
* int -> 3
* float ->3.56
* str -> ""
* bool -> True False

___

**Dyamic Typing**
```python
name= "Aryan"
name = 20
```

___

**Composite Data Types**
* List -> Array (Lists can be heterogenous)
* Dictionary -> Key-value pairs
* Tuples -> Lists (Immutability); immutable = constant, cant change
* Class -> blueprint of an object

**Lists**
marks = [20,30,40,50]
[32.5,30,"thirty]


**Tuples**
marks = (20,30,40,50)

**Dictionary**
dictionary={
    "name": "John",
    "age":24,
    "married":False
}

____
lists can nest other lists,
dictionary can nest dictionary, and lists

**Decision Flow and Branching**
* If/else:
```
if(<condn>):
    print("This is cond1)
else:
    print("This is cond2)
```

* If/elif/else
```
if(<condn>):
    print("This is cond1)
elif:
    print("This is elif)
else:
    print("This is else)
```

* While loop:
1. Stopping condition should exist.
2. Infinite loops must be prevented
3. Variable used for condition must be change inside the loop

* For loop:
```
li = [a,b,c,d,e]
for item in li:
    print(item)
    print(f"The item is {item}")
```

* 100 sequentially  
```
for i in range(start,stop, range):
    statement
```