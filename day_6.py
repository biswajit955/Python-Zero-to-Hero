# Day 6 Assignment : Floor divison of any two number by using Decorators.

def decorators(fun):
	def deno(num1, num2):
		if num1 < num2 :
			num1, num2 = num2, num1
		return fun(num1, num2)
	return deno
	
@decorators
def div(num1, num2):
	return  num1 // num2

num1 =int(input("Enter two Nunbers: "))
num2 =int(input("Enter two Nunbers: "))
print(num1,num2)


print(div(num1, num2))