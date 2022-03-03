import math

for name in dir(math):  # module the module has to have been previously imported as a whole ( not from module )
    print(name, end='\t')
    # prints (__doc__	__loader__	__name__	__package__	__spec__	acos	acosh	asin ... )


""" The first group of the math's functions are connected with trigonometry:

sin(x) → the sine of x;
cos(x) → the cosine of x;
tan(x) → the tangent of x.

asin(x) → the arcsine of x;
acos(x) → the arccosine of x;
atan(x) → the arctangent of x.

pi → a constant with a value that is an approximation of π;
radians(x) → a function that converts x from degrees to radians;
degrees(x) → acting in the other direction (from radians to degrees)

sinh(x) → the hyperbolic sine;
cosh(x) → the hyperbolic cosine;
tanh(x) → the hyperbolic tangent;
asinh(x) → the hyperbolic arcsine;
acosh(x) → the hyperbolic arccosine;
atanh(x) → the hyperbolic arctangent.

e → a constant with a value that is an approximation of Euler's number (e) ~= 2.71828
exp(x) → finding the value of e^x; ~= 2.71828^x
log(x) → the natural logarithm of x
log(x, b) → the logarithm of x to base b
log10(x) → the decimal logarithm of x (more precise than log(x, 10))
log2(x) → the binary logarithm of x (more precise than log(x, 2))

pow(x, y) → finding the value of x^y (mind the domains)

The last group consists of some general-purpose functions like:

ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
floor(x) → the floor of x (the largest integer less than or equal to x)
trunc(x) → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor)
factorial(x) → returns x! (x has to be an integral and not a negative)
hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y (the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise)
"""

print('\n')
print(math.exp(2))
# 7.38905609893065

print(math.e)
# 2.718281828459045


