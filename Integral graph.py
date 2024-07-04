import matplotlib.pyplot as plt
import numpy as np

# Function to be integrated
def f(x):
    return np.sin(x)  # Example function

# Range for x values
x = np.linspace(0, 2*np.pi, 100)

# Plotting the function
plt.plot(x, f(x), label='$f(x) = \sin(x)$', color='#F37D34')
plt.fill_between(x, f(x), color='#7D34F3', alpha=0.3, label='Area under $f(x)$')

# Highlight the area under the curve between 0 and 2*π
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title('Graphical Meaning of an Integral')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.show()
