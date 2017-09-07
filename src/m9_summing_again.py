"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Hui Chen.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_powers()
    test_sum_powers_in_range()


def test_sum_powers():
    """ Tests the   sum_powers   function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function.
    #   It TESTS the  sum_powers  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers   function:')
    print('--------------------------------------------------')

    # Test :
    expected1 = 3.80826
    answer1 = sum_powers(5, -0.3)
    print('Test 1 expected:', expected1)
    print('       actual:  ', answer1)

    expected2 = 0
    answer2 = sum_powers(0, 0.3)
    print('Test 2 expected:', expected2)
    print('       actual:  ', answer2)

    expected3 = 144.45655
    answer3 = sum_powers(100, 0.1)
    print('Test 3 expected:', expected3)
    print('       actual:  ', answer3)


def sum_powers(n, p):
    """
    What comes in:  A non-negative integer n
                    and a number p.
    What goes out:  The sum   1**p + 2**p + 3**p + ... + n**p
       for the given numbers n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:   None.
    Examples:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    sum1 = 0
    for k in range(n):
        sum1 = sum1 + (k + 1)**p

    return sum1


def test_sum_powers_in_range():
    """ Tests the   sum_powers_in_range   function. """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this function.
    #   It TESTS the  sum_powers_in_range  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers_in_range   function:')
    print('--------------------------------------------------')

    # Test :
    expected1 = 1
    answer1 = sum_powers_in_range(1, 1, 1)
    print('Test 1 expected:', expected1)
    print('       actual:  ', answer1)

    expected2 = 5
    answer2 = sum_powers_in_range(1, 2, 2)
    print('Test 2 expected:', expected2)
    print('       actual:  ', answer2)

    expected3 = 142.384776
    answer3 = sum_powers_in_range(3, 100, 0.1)
    print('Test 3 expected:', expected3)
    print('       actual:  ', answer3)


def sum_powers_in_range(m, n, p):
    """
    What comes in:  Non-negative integers m and n, with n >= m,
                    and a number p.
    What goes out:  the sum
           m**p + (m+1)**p + (m+2)**p + ... + n**p
       for the given numbers m, n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:  None.
    Example:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers_in_range  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    #
    # COMMENT: Do you see how you could use   sum_powers_in_range
    #    to test  sum_powers   and (to a lesser extent) vice-versa?
    # ------------------------------------------------------------------
    sum2 = 0
    for k in range(n):
        sum2 = sum2 + (k + 1)**p

    sum3 = 0
    for k in range(m-1):
        sum3 = sum3 + (k + 1)**p

    sum4 = sum2 - sum3

    return sum4

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
