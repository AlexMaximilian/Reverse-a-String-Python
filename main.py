#Alex Maximilian
#Simple string reversal script using slicing


def reverse_a_string(x):
  return x[::-1]

x = input("Input your text you want to reverse")
mytxt = reverse_a_string(x)

print("Your orignal text was", x, "backwards it is", mytxt)

