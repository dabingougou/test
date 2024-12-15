# Python code to find unique prime factors

n = 1234567890

def find_factors(n):
  m = 1
  p = 1
  if n <= 0:
    return 0
  else:
        while m < n:
            m += 1 
            
    while n%(p + 1) == 0:
      p += 1
# To be completed

   

