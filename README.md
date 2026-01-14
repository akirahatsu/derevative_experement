# derevative_experement

f'(x) = (f(x+▲x) - f(x))/▲x
for explonentials
f'(x) = (f(x)*f(▲x) -f(x))/▲x

▲x == 1e - 6 not infinitysmal  ... coz...:)

Why I made it

Honestly, this started as curiosity. I wanted to feel what it’s like to “teach Python calculus” directly and see what happens when I make mistakes, debug them, and iterate.

Even if the code isn’t mathematically perfect or robust for all edge cases, it helped me understand derivatives, exponentials, and logarithms in a way that watching tutorials never did.

How to use

Import or run derivative() in your Python environment

Provide a function as a string (e.g., "x**2-2*x")

Call the function with a number for x

Experiment with h to see the effect of step size

example :
derivative(2, operation="x**2-2*x")
