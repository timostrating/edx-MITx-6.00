# Lecture 3

|Data  | operations |commands
| --- | --- | --- |
|Numbers | / * + -| input / output
|Strings | and, or|conditionals
|Booleans | ** this is ^ |while


```python
x = 10
for i in range(1, x):
	if x % i == 0:
		print 'divisor ', i
```


__tuple__ orded sequence of elements
```python
myList = [1, 2, 3, 4, 5]
mytuple = (1, 2, 3, 4, 5)

mytuple[-1] --> 5
mytuple[1:3] --> [2, 3]
mytuple[:3] --> [1, 2, 3]
mytuple[3:] --> [3, 4, 5]
```


```python
sum = 0
for ch in str(1952):
	sum += int(ch)

print sum
```
