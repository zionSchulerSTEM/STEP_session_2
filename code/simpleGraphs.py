# Import statements for the libraries being used
import numpy as np
import matplotlib.pyplot as plt


# Create an array of a 100 numbers from 0 and 10 that are evenly spaced apart
x = np.linspace(0, 10, 100)
# y is an array where y = f(x) = x^2
y = np.square(x)

# Generate the graph of y = f(x) = x^2, a simple polynomial
plt.plot(x, y)
plt.show()

# Now that we have x, we can generate graphs for the other analytic functions

# y_cos = f(x) = cos(x)
y_cos = np.cos(x)

# Generate the graph of y = f(x) = cos(x), a simple trig function
plt.plot(x, y_cos)
plt.show()

# y_exp = f(x) = e^x
y_exp = np.exp(x)

# Generate the graph of y = f(x) = e^x, a simple exponential
plt.plot(x, y_exp)
plt.show()

# y_exp = f(x) = log(x)
y_exp = np.log(x)

# Generate the graph of y = f(x) = log(x), a simple logarithm
plt.plot(x, y_exp)
plt.show()
