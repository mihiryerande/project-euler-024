# Problem 24:
#     Lexicographic Permutations
#
# Description:
#     A permutation is an ordered arrangement of objects.
#     For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
#     If all of the permutations are listed numerically or alphabetically,
#       we call it lexicographic order
#
#     The lexicographic permutations of 0, 1 and 2 are:
#         012   021   102   120   201   210
#
#     What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from math import factorial


def main(n: int) -> str:
    """
    Returns the `n`th lexicographically-ordered permutation of the digits 0123456789

    Args:
        n (int): Index of desired permutation in lexicographic ordering (natural number)

    Returns:
        (str): `n`th lexicographically-ordered permutation of 0123456789

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0
    n -= 1

    # Iteratively construct permutation by individual digits
    perm = []
    digits = list(map(str, range(10)))  # Available digits
    remaining_perms = factorial(len(digits))  # Number of possible perms overall
    while len(digits) > 0:
        remaining_perms //= len(digits)  # Remaining perms if one char were fixed
        i, n = divmod(n, remaining_perms)
        perm.append(digits.pop(i))
    return ''.join(perm)


if __name__ == '__main__':
    perm_num = int(input('Enter a natural number: '))
    nth_perm = main(perm_num)
    print('Permutation #{} of "0123456789" in lexicographic ordering:'.format(perm_num))
    print('  {}'.format(nth_perm))
