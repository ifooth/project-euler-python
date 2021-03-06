# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import datetime
import functools
import itertools
import logging
import math
import operator

from euler.lib import _int, data

LOG = logging.getLogger(__name__)


def problem_1():
    """
    Multiples of 3 and 5
    3的倍数和5的倍数
    """
    return sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)


def problem_2():
    """
    Even Fibonacci numbers
    偶斐波那契数
    """
    even_fibonacci = []
    for fib in _int.fibonacci_generator(1, 2):
        if fib % 2 == 0:
            even_fibonacci.append(fib)
        if fib > 4000000:
            return sum(even_fibonacci)


def problem_3():
    """
    Largest prime factor
    最大质因数
    """
    return max(_int.factors_generator(600851475143))


def problem_4():
    """
    Largest palindrome product
    最大回文乘积
    """
    all_numbers = map(
        lambda x: x[0] * x[1],
        itertools.product(range(100, 1000), range(100, 1000)))
    return max(filter(_int.is_palindromic, all_numbers))


def problem_5():
    """
    Smallest multiple
    最小倍数
    """
    factors = {1: 1}
    for i in range(1, 20):
        for key, value in _int.factors(i).items():
            if key not in factors or value > factors[key]:
                factors[key] = value
    return functools.reduce(
        operator.mul, (key ** value for key, value in factors.items()))


def problem_6():
    """Sum square difference
    平方的和与和的平方之差
    """
    return abs(
        sum(i ** 2 for i in range(1, 101)) -
        sum(i for i in range(1, 101)) ** 2)


def problem_7():
    """
    10001st prime
    第10001个素数
    """
    count, num = 2, 3
    while count != 10001:
        num += 2
        if _int.is_prime(num):
            count += 1
    return num


def problem_8():
    """
    Largest product in a series
    连续数字最大乘积
    """
    data_file = "problem_8.txt"
    num_str = map(int, ''.join(data.get_file(data_file).strip().splitlines()))
    return max(
        functools.reduce(operator.mul, num_str[i:i + 13])
        for i in range(len(num_str) - 12))


def problem_9():
    """
    Special Pythagorean triplet
    特殊毕达哥拉斯三元组
    """
    for i in range(1, 1000):
        for j in range(i, 1000):
            if i ** 2 + j ** 2 == (1000 - i - j) ** 2:
                return i * j * (1000 - i - j)


def problem_10():
    """
    Summation of primes
    素数的和
    """
    return sum(filter(_int.is_prime, range(3, 2000000, 2))) + 2


def problem_11():
    """
    Largest product in a grid
    方阵中的最大乘积
    """
    data_file = "problem_11.txt"

    def max_row(row):
        return max(functools.reduce(
            operator.mul, row[i: i + 4]) for i in range(len(row) - 3))
    grid = [map(int, i.split()) for i in data.get_file(data_file).strip().splitlines()]
    max_product = 0
    # 计算每行
    for row in grid:
        LOG.debug(row)
        if max_row(row) > max_product:
            max_product = max_row(row)
    # 计算每列
    column_grid = [[row[i] for row in grid] for i in range(20)]
    for column in column_grid:
        LOG.debug(column)
        if max_row(column) > max_product:
            max_product = max_row(column)
    # 计算右对角线 /
    right_diagonal_grid = []
    for i in range(3, 20):
        up_diagonal = [grid[i - count][count] for count in range(i + 1)]
        LOG.debug(up_diagonal)
        right_diagonal_grid.append(up_diagonal)
    for i in range(16):
        down_diagonal = [
            grid[count][20 - count + i] for count in range(19, i, -1)]
        LOG.debug(down_diagonal)
        right_diagonal_grid.append(down_diagonal)
    for row in right_diagonal_grid:
        if max_row(row) > max_product:
            max_product = max_row(row)
    # 计算左对角线 \
    left_diagonal_grid = []
    for i in range(16, -1, -1):
        up_diagonal = [grid[i + count][count] for count in range(0, 20 - i)]
        LOG.debug(up_diagonal)
        left_diagonal_grid.append(up_diagonal)
    for i in range(16):
        down_diagonal = [
            grid[count - i - 1][count] for count in range(i + 1, 20)]
        LOG.debug(down_diagonal)
        left_diagonal_grid.append(down_diagonal)
    for row in left_diagonal_grid:
        if max_row(row) > max_product:
            max_product = max_row(column)
    return max_product


def problem_12():
    """
    Highly divisible triangular number
    高度可约的三角形数
    """
    num = [1, 1]
    while len(_int.positive_divisors(num[1])) <= 500:
        num[0] += 1
        num[1] += num[0]
    return num[1]


def problem_13():
    """
    Large sum
    大和
    """
    data_file = "problem_13.txt"
    return int(str(sum(map(int, data.get_file(data_file).strip().splitlines())))[:10])


def problem_14():
    """
    Longest Collatz sequence
    最长考拉兹序列
    """
    result = [0, 0]
    for i in range(2, 1000000):
        raw_value = i
        count = 0
        while i != 1:
            # 偶数做&运算是0，奇数是1
            if i & 1:
                i = i * 3 + 1
            else:
                i //= 2
            count += 1
        else:
            if result[0] < count:
                result = [count, raw_value]
    return result[1]


def problem_15():
    """
    Lattice paths
    网格路径
    """
    return math.factorial(40) // (math.factorial(20) ** 2)


def problem_16():
    """
    Power digit sum
    幂的数字和
    """
    return sum(map(int, str(2 ** 1000)))


def problem_17():
    """
    Number letter counts
    表达数字的英文字母计数
    """
    num_word = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand',
        'and': 'and'
    }
    letters = ''
    # 计算1~100
    for i in range(1, 100):
        if i in num_word:
            letters += num_word[i]
        else:
            letters += (num_word[i // 10 * 10] + num_word[i % 10])
    hundred_letters = letters
    # 计算100~999
    for j in range(1, 10):
        # one hundred and one
        letters += (num_word[j] * 99 + num_word[100] * 99 +
                    num_word['and'] * 99 + hundred_letters)
        # one hundred
        letters += (num_word[j] + num_word[100])
    # 计算1000 one thousand
    letters += num_word[1] + num_word[1000]  # 1000
    return len(letters)


def problem_18():
    """
    Maximum path sum I
    最大路径和 I
    关键字：动态规划，递归，至底向上消俄罗斯方块
    参考问题81
    """
    data_file = "problem_18.txt"
    binary_tree = list(map(int, i.split())
                       for i in data.get_file(data_file).strip().splitlines())

    def helper(tree, leaf):
        LOG.debug(leaf)
        if len(leaf) == 1:
            return leaf
        else:
            root = tree.pop(-1)
            for idx, num in enumerate(root):
                left = num + leaf[idx]
                right = num + leaf[idx + 1]
                root[idx] = max([left, right])
            leaf = root
            return helper(tree, leaf)

    leaf = binary_tree.pop(-1)
    return helper(binary_tree, leaf)[0]


def problem_19():
    """
    Counting Sundays
    数星期日
    Monday is 0 and Sunday is 6.
    """
    return len(filter(
        lambda x: datetime.date(x[0], x[1], 1).weekday() == 6,
        [(year, month) for month in range(1, 13) for year in range(1901, 2001)]))  # noqa


def problem_20():
    """
    Factorial digit sum
    阶乘数字和
    """
    return sum(map(int, str(math.factorial(100))))


def problem_21():
    """
    Amicable numbers
    亲和数
    """
    return sum(filter(
        lambda x: x != sum(_int.proper_divisors(x)) and
        x == sum(_int.proper_divisors(sum(_int.proper_divisors(x)))),
        range(2, 10000)))


def problem_22():
    """
    Names score
    姓名得分
    """
    names = sorted(map(
        lambda x: x.strip('"'), data.get_file('names.txt').strip().split(',')))
    return sum(map(
        lambda x: (x[0] + 1) * sum(map(lambda y: ord(y) - 64, x[1])),
        enumerate(names)))


def problem_23():
    """
    Non-abundant sums
    并非盈数之和
    """
    abundants = filter(lambda x: sum(_int.proper_divisors(x)) > x, range(1, 28123))

    return sum(i for i in range(1, 28124) if not any(i - a in abundants for a in abundants))


def problem_24():
    """
    Lexicographic permutations
    字典序排列
    """
    letters = '0123456789'
    return int(''.join(sorted(itertools.permutations(letters, 10))[1000000 - 1]))


def problem_25():
    """
    1000-digit Fibonacci number
    一千位斐波那契数
    """
    count = 0
    for fib in _int.fibonacci_generator():
        count += 1
        if len(str(fib)) == 1000:
            return count
