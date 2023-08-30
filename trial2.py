def read_polynomial(num_variables, degree):
    """
    Reads a multilinear polynomial from the user.

    Args:
        num_variables (int): The number of variables in the polynomial.
        degree (int): The degree of the polynomial.

    Returns:
        A list containing the coefficients of the monomials in the polynomial.
    """
    num_monomials = 2 ** num_variables
    polynomial = [0] * num_monomials

    for i in range(num_monomials):
        monomial = []
        for var in range(num_variables):
            power = (i >> var) & 1
            monomial.append(power)
        coeff = input(f"Enter the coefficient for the monomial {tuple(monomial)}: ")
        polynomial[i] = int(coeff)

    return polynomial


def read_partial_assignment(num_variables):
    """
    Reads a partial assignment from the user.

    Args:
        num_variables (int): The number of variables in the polynomial.

    Returns:
        A dictionary containing the partial assignment of variables.
    """
    partial_assignment = {var: 0 for var in range(num_variables)}
    for var in range(num_variables):
        val = input(f"Enter the assignment for variable {var}: ")
        partial_assignment[var] = int(val)

    return partial_assignment


def restricted_polynomial(polynomial, partial_assignment):
    """
    Computes the restricted polynomial of a multilinear polynomial over F2.

    Args:
        polynomial (list): A list containing the coefficients of the monomials in the polynomial.
        partial_assignment (dict): A dictionary containing the partial assignment of variables.

    Returns:
        A list containing the coefficients of the monomials in the restricted polynomial.
    """
    num_variables = len(partial_assignment)
    num_monomials = 2 ** num_variables
    restricted_poly = [0] * num_monomials

    for i in range(num_monomials):
        monomial = []
        coeff = polynomial[i]
        for var in range(num_variables):
            power = (i >> var) & 1
            if var in partial_assignment and partial_assignment[var] != power:
                coeff = 0
                break
            monomial.append(power)
        if coeff != 0:
            restricted_poly[i] = coeff

    return restricted_poly


if __name__ == "__main__":
    num_variables = int(input("Enter the number of variables in the polynomial: "))
    degree = int(input("Enter the degree of the polynomial: "))

    polynomial = read_polynomial(num_variables, degree)
    print(f"Polynomial: {polynomial}")

    partial_assignment = read_partial_assignment(num_variables)
    print(f"Partial assignment: {partial_assignment}")

    restricted_poly = restricted_polynomial(polynomial, partial_assignment)
    print(f"Restricted polynomial: {restricted_poly}")
