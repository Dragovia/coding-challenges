# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

def fib_2(n,memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1,memo) + fib_2(n-2,memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n,memo)
#-------------------------------------------------
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

##def factorial(n):
    #if n < 0:
     #   return -1
   # elif n == 0:
     #   return 1
    #else:
       ## return n * factorial(n-1)

#def permutation(str):
   # permutation(str,"")

#def permutation(str,prefix):
   # if str.len() == 0:
      #  print(prefix)
   # else:
       # for x in str.length():
         #   rem = str[0:x] + str[x+1]
           # permutation(rem, prefix + str[x])

def TwoStones (names):
    if (names % 2) == 0:
        return("Bob")
    else:
        return("Alice")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #print(fib(50))
    #print(fib_memo(50))
   # print(fib_bottom_up(1000))
   #print(factorial(3))
   # print(permutation("dog","o"))
    num = int(input(""))
    print(TwoStones(num))