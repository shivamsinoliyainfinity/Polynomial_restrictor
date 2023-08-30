from itertools import product

def restricted_polynomial(polynomial, partial_assignment):
    """
    Computes the restricted polynomial given a multilinear polynomial and a partial assignment.

    Args:
        polynomial (dict): A dictionary containing the coefficients of the polynomial.
        partial_assignment (dict): A dictionary containing the partial assignment of variables.

    Returns:
        A dictionary containing the coefficients of the restricted polynomial.
    """
    v = len(partial_assignment)
    restricted_poly = {tuple(0 for _ in range(v)): 0}

    for monomial, coefficient in polynomial.items():
        include_monomial = True
        for var, val in partial_assignment.items():
            if monomial[var] != val:
                include_monomial = False
                break
        if include_monomial:
            restricted_poly[tuple(monomial[var] for var in range(v))] = coefficient

    return restricted_poly

def read_polynomial():
    """
    Reads a multilinear polynomial from the user.

    Returns:
        A dictionary containing the coefficients of the polynomial.
    """
    polynomial = {}
    num_variables = int(input("Enter the number of variables: "))
    degree = int(input("Enter the degree of the polynomial: "))

    for _ in range(2**num_variables):
        monomial = tuple(int(x) for x in bin(_)[2:].zfill(num_variables))
        if sum(monomial) <= degree:
            coefficient = int(input(f"Enter the coefficient for the monomial {monomial}: "))
            polynomial[monomial] = coefficient

    return polynomial


def read_partial_assignment(num_variables):
    """
    Reads a partial assignment from the user.

    Args:
        num_variables (int): The number of variables in the polynomial.

    Returns:
        A dictionary containing the partial assignment of variables.
    """
    partial_assignment = {}
    for var in range(num_variables):
        val = input(f"Enter the assignment for variable {var}: ")
        partial_assignment[var] = int(val)

    return partial_assignment
if __name__ == '__main__':
    polynomial = read_polynomial()
    num_variables = len(list(polynomial.keys())[0])
    partial_assignment = read_partial_assignment(num_variables)
    restricted_poly = restricted_polynomial(polynomial, partial_assignment)
    print(restricted_poly)
