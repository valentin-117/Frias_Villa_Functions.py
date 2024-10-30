def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(8, 2, c = 10, d = 89)