
stack = [];

# Function to push digits into stack
def push(number):

	while (number != 0):
		stack.append(number % 10);
		number = int(number / 10);

# Function to reverse the number
def reverse_number(number):

	# Function call to push number's
	# digits to stack
	push(number);

	reverse = 0;
	i = 1;

	# Popping the digits and forming
	# the reversed number
	while (len(stack) > 0):
		reverse = reverse + (stack[len(stack) - 1] * i);
		stack.pop();
		i = i * 10;

	# Return the reversed number formed
	return reverse;

number = 3479;

# Function call to reverse the number number
print(reverse_number(number));
