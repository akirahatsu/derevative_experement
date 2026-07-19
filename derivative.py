def derivative(x, h=1e-6, operation="x**2"):
    """
    Numerically computes the derivative of a function using
    the finite difference formula:

        f'(x) ≈ (f(x+h) - f(x)) / h

    Parameters
    ----------
    x : float
        Point where the derivative is evaluated.
    h : float, optional
        Small step size.
    operation : str, optional
        Function as a string using variable 'x'.

    Examples
    --------
    derivative(2, operation="x**2")
    derivative(2, operation="2**x - 2*x")
    derivative(3, operation="x**3 + 5*x - 1")
    """

    operation = operation.replace("^", "**")

    env = {"x": x}
    env_h = {"x": x + h}

    return (eval(operation, {}, env_h) - eval(operation, {}, env)) / h



print(derivative(2, operation="x**2"))
# ≈ 4.000001

print(derivative(2, operation="2**x - 2*x"))
# ≈ -1.22741

print(derivative(3, operation="x**3 + 5*x"))
# ≈ 32
