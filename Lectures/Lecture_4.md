# Lecture 4

int
ArbetraryPrecision
Long
floating point numbers


mantissa (floating point)  64 bit
1 <= mantissa <= 2   
-1022:1023	exponent
*	 1 bit sign  
*	11 exponent
*	52 mantissa


#### Decomposition

#### Abstraction


###### Function
python useses the keyword def to define a function
* has a name
* has parameter (o or more)
* has a docstring (optional)
* has a body

```python
def is_even( i):
	"""    <-- this is a docstring
	input: i, a positive int
	Returns True if i is even, otherwise False
	"""
	print ("this is the body of is_even()")
	return 1 % 2 == 0

is_even(3)
```
