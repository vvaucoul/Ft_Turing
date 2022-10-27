# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_complexity.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vvaucoul <vvaucoul@student.42.Fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/29 14:57:04 by mle-faou          #+#    #+#              #
#    Updated: 2022/10/28 01:08:01 by vvaucoul         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math
from ft_turing import ft_turing
import matplotlib.pyplot as plt
# pip install --upgrade matplotlib

def find_complexity():
    """Find the complexity of a Turing Machine and display a graph comparing it the Big-O complexity chart.
    """
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Plot the Big-O complexity chart
    x_coords = [x for x in range(1, 101)]

    # O(1)
    o1_y_coords = [1 for x in x_coords]
    ax.plot(x_coords, o1_y_coords, color = "orange", label = "O(1)")

    # O(logn)
    ologn_y_coords = [math.log(x) for x in x_coords]
    ax.plot(x_coords, ologn_y_coords, color = "cyan", label = "O(logn)")

    # O(n)
    on_y_coords = [x for x in x_coords]
    ax.plot(x_coords, on_y_coords, color = "purple", label = "O(n)")

    # O(nlogn)
    onlogn_y_coords = [x * math.log(x) for x in x_coords]
    ax.plot(x_coords, onlogn_y_coords, color = "green", label = "O(nlogn)")

    # O(n^2)
    on2_y_coords = [x ** 2 for x in x_coords]
    ax.plot(x_coords, on2_y_coords, color = "red", label = "O(n^2)")

    # O(2^n)
    o2n_y_coords = [2 ** x for x in x_coords]
    ax.plot(x_coords, o2n_y_coords, color = "blue", label = "O(2^n)")

    # O(n!)
    onf_y_coords = [math.factorial(x) for x in x_coords]
    ax.plot(x_coords, onf_y_coords, color = "brown", label = "O(n!)")
    
    # Plot the complexity of the Turing Machine

    # unary_sub
    unary_sub_y_coords = []
    for x in x_coords:
        unary_sub_y_coords.append(ft_turing("machines/unary_sub.json", "{}-{}=".format(x * "1", x * "1"), mode = "sample"))
        if unary_sub_y_coords[-1:][0] > 1000:
            for _ in range(x, 100):
                unary_sub_y_coords.append(unary_sub_y_coords[-1:][0])
            break
    ax.plot(x_coords, unary_sub_y_coords, "--", color = "red", label = "unary_sub")

    # unary_sub
    unary_sub_y_coords2 = []
    for x in x_coords:
        unary_sub_y_coords2.append(ft_turing("machines/unary_sub.json", "{}-1=".format(x * "1"), mode = "sample"))
        if unary_sub_y_coords2[-1:][0] > 1000:
            for _ in range(x, 100):
                unary_sub_y_coords2.append(unary_sub_y_coords2[-1:][0])
            break
    ax.plot(x_coords, unary_sub_y_coords2, "-.", color = "red", label = "unary_sub2")

    # unary_add
    unary_add_y_coords = []
    for x in x_coords:
        unary_add_y_coords.append(ft_turing("machines/unary_add.json", "{}+{}=".format(x * "1", x * "1"), mode = "sample"))
        if unary_add_y_coords[-1:][0] > 1000:
            for _ in range(x, 100):
                unary_add_y_coords.append(unary_add_y_coords[-1:][0])
            break
    ax.plot(x_coords, unary_add_y_coords, "--", color = "blue", label = "unary_add")

    # palindrome
    palindrome_y_coords = []
    for x in x_coords:
        palindrome_y_coords.append(ft_turing("machines/palindrome.json", "1{}1".format(x * "0"), mode = "sample"))
        if palindrome_y_coords[-1:][0] > 1000:
            for _ in range(x, 100):
                palindrome_y_coords.append(palindrome_y_coords[-1:][0])
            break
    ax.plot(x_coords, palindrome_y_coords, "--", color = "green", label = "palindrome")

    # palindrome2
    palindrome_y_coords2 = []
    for x in x_coords:
        palindrome_y_coords2.append(ft_turing("machines/palindrome.json", "{}1{}".format(x * "0", x * "0"), mode = "sample"))
        if palindrome_y_coords2[-1:][0] > 1000:
            for _ in range(x, 100):
                palindrome_y_coords2.append(palindrome_y_coords2[-1:][0])
            break
    ax.plot(x_coords, palindrome_y_coords2, "-.", color = "green", label = "palindrome2")
    
    # equal
    equal_y_coords = []
    for x in x_coords:
        equal_y_coords.append(ft_turing("machines/equal.json", "{}{}".format(x * "0", x * "1"), mode = "sample"))
        if equal_y_coords[-1:][0] > 1000:
            for _ in range(x, 100):
                equal_y_coords.append(equal_y_coords[-1:][0])
            break
    ax.plot(x_coords, equal_y_coords, "--", color = "purple", label = "equal")

    # is_pair
    is_pair_y_coords = []
    for x in x_coords:
        is_pair_y_coords.append(ft_turing("machines/is_pair.json", "{}".format(x * "0"), mode = "sample"))
        if is_pair_y_coords[-1:][0] > 1000:
            for _ in range(x, 100):
                is_pair_y_coords.append(is_pair_y_coords[-1:][0])
            break
    ax.plot(x_coords, is_pair_y_coords, "--", color = "orange", label = "is_pair")

    ax.set_xlabel('Elements')
    ax.set_xlim([0, 100])
    ax.set_ylabel('Operations')
    ax.set_ylim([0, 1000])
    ax.set_title('Big-O Complexity Chart')
    plt.legend(loc = 'upper right')
    plt.grid(axis = 'y')
    plt.show()

if __name__ == "__main__":
    find_complexity()

