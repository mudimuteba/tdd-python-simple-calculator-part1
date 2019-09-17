import simple_calculator

def test_add_two_numbers():
	"""it can add 2 numbers"""
	assert simple_calculator.add(0, 0) == 0
	assert simple_calculator.add(-1, -1) == -2
	assert simple_calculator.add(4, 5) == 9

def test_add_many_numbers():
	"""it can add many numbers"""
	assert simple_calculator.add(10, 20, 30) == 60
	assert simple_calculator.add(-20, 10) == -10

def test_multiply_two_numbers():
	"""it can multiply 2 numbers"""
	assert simple_calculator.multiply(10, 2) == 20

def test_multiply_many_numbers():
	"""it can multiply lots of numbers"""
	assert simple_calculator.multiply(2, -3, 2, -3) == 36