def compute_sum(n) :

    result = 0   # initialize result

    # One by one compute sum of digits
    # in every number from 1 to n
    for x in range(1, n+1) :
        result = result + sumOfDigits(x)

    return result


def sumOfDigits(x) :
	sum = 0
	while (x != 0) :
		sum = sum + x % 10
		x = x // 10

	return sum



print(compute_sum(3))
