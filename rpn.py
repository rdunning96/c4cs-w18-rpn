#/usr/bin/env python3

import operator

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.trudiv,
	'^': operator.pow,
}

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result
		print(stack)
	return stack.pop() 


def main():
	while True:
		result = calculate(input("rpn calc> "))
		print("Result: ", result)


if __name__ == '__main__':
	main()
