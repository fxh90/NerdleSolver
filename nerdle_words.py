"""
Generate strings of expressions that are mathematically correct and has the length of 8.
^-?[0-9]{1,3}([\+-\*/][0-9]{1,3}){1,2}=-?[0-9]{1,3}$
"""

import itertools

__author__ = "Z Feng"

digits = [str(i) for i in range(10)]
two_digits = [''.join(i) for i in itertools.product(digits, repeat=2)]
three_digits = [''.join(i) for i in itertools.product(digits, repeat=3)]

p1 = digits + two_digits + three_digits
p1 += ['-' + i for i in p1]

print('p1:', len(p1))

p2 = ['+' + i for i in p1]
p2 += ['-' + i for i in p1]
p2 += ['*' + i for i in p1]
p2 += ['/' + i for i in p1 if not i in ('0', '00', '000', '-0', '-00', '-000')]

print('p2:', len(p2))

lfs_two_parts = [i for i in itertools.product(p1, p2) if len(''.join(i)) <=6]
print('lfs_two_parts:', len(lfs_two_parts))

p1_three_parts = [i for i in p1 if len(i) <= 2]
print('p1_three_parts:', len(p1_three_parts))
p2_three_parts = [i for i in p2 if len(i) <= 3]
print('p2_three_parts:', len(p2_three_parts))

lfs_three_parts = [i for i in itertools.product(p1_three_parts, p2_three_parts, p2_three_parts) if len(''.join(i)) <=6]
print('lfs_three_parts:', len(lfs_three_parts))

lfs = lfs_two_parts + lfs_three_parts
print('lfs:', len(lfs))


def eval_in_parts(lfs):
	lfs_str = 'int("' + lfs[0] + '")' + lfs[1][0] + 'int("' + lfs[1][1:] + '")'
	if len(lfs) == 3:
		lfs_str += lfs[2][0] + 'int("' + lfs[2][1:] + '")'
	return eval(lfs_str)

rhs = [str(eval_in_parts(i)) for i in lfs]
print('evaluated')

expr = [''.join(lfs[i]) + '=' + rhs[i] for i in range(len(lfs))]
valid_expr = [i for i in expr if len(i) <= 8]
print('valid_expr:', len(valid_expr))

def fill_to_len(expr, length=8):
	to_fill = length - len(expr)
	if to_fill:
		lfs, rhs = expr.split('=')
		expr = lfs + '=' + '0' * to_fill + rhs
	return expr

expr_len_8 = list(map(fill_to_len, valid_expr))

with open('nerdle_words.txt', 'w') as f:
	for e in expr_len_8:
		f.write(e + '\n')

# EOF
