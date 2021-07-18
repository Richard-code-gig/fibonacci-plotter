from decorator3 import Decorate, Profile
import itertools, random

function = Decorate.function

def fast_fib(n: int, *args, memo: dict = {}) -> int: #The decorator wont work for this function because of the dict
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]    
    memo[n] = fast_fib(n-1, memo) + fast_fib(n-2, memo)
    return memo[n]

@function #Decorator
def omnipotent_fibo(n):
    if n == 1 or n == 2: return 1
    result = [None] * (n+1)
    result[1] = 1
    result[2] = 1
    for i in range(3, n+1):
        result[i] = result[i -1] + result[i-2]
    return result[n]

@function
def fib(n):
    n_0, n_1, i = 1, 1, 2
    while i < n:
        n_2 = n_0 + n_1
        n_0, n_1 = n_1, n_2
        i += 1
    if n == 1 or n == 2:
        return 1
    else:
        return n_2

@function
def fib_Ala(n):
    s = [0, 1]
    s += [(s := [s[1], s[0] + s[1]]) and s[1] for _ in range(n-1)]
    return s[n]


profile1 = Profile()

profile1.marker = itertools.cycle(('o', '>', '2'))
profile1.color = itertools.cycle(('r', 'b', 'y'))
profile1.label = itertools.cycle(("omnipotent_fibo", "fib", "fib_Ala"))
profile1.linestyle = itertools.cycle(('-', ':', '--'))

def main():
    for _ in random.sample(range(100), k=5): #generate 5 images to be saved in the file described in profile_builder
        a = "log(time)" #xlabel
        b = "log(fibonacci)" #ylabel
        c = "Timing fibonacci" #Title
        model = [omnipotent_fibo(50), fib(50), fib_Ala(50)] # n = number passed to fibonacci functions
        profile1.profile_builder(a, b, c, model, saver='fibonacci-plotter/new_fib_img')

if __name__ == '__main__':
    main()