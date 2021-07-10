from time import perf_counter_ns
import math, random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
plt.rcParams["figure.figsize"] = (8, 4.7)

#The program aims to investigate the execution time of some fibonacci functions
      
def fast_fib(n: int, *args, memo: dict = {}) -> int:
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]    
    memo[n] = fast_fib(n-1, memo) + fast_fib(n-2, memo)
    return memo[n]

def omnipotent_fibo(n):
    if n == 1 or n == 2: return 1
    result = [None] * (n+1)
    result[1] = 1
    result[2] = 1
    for i in range(3, n+1):
        result[i] = result[i -1] + result[i-2]
    return result[n]

def fib(n):
    for x in range(10):
        n_0, n_1, i = 1, 1, 2
        while i < n:
            n_2 = n_0 + n_1
            n_0, n_1 = n_1, n_2
            i += 1
        if n == 1 or n == 2:
            return 1
        else:
            return n_2


def fib_Ala(n):
    s = [0, 1]
    s += [(s := [s[1], s[0] + s[1]]) and s[1] for _ in range(n-1)]
    return s[n]

"""The 4 functions below modifies the fibonacci functions to generate list Iterators and collect the log time differences
between execution. E.g., the rate between generating values, say, 10, 15, 20, etc.
"""

def modify_fast_fib():
    for _ in range(500): #run 1000 iterations. Set higher or lower depending on machine spec to get statistical precision
        t1 = perf_counter_ns()
        s_ff = [],[]
        for i in range(10,50,5):
            s_ff[0].append(math.log(fast_fib(i)))
            s_ff[1].append(math.log(perf_counter_ns() - t1))
    return s_ff

def modify_omnipotent_fibo():
    for _ in range(500):
        t1 = perf_counter_ns()
        s_of = [],[]
        for i in range(10,50,5):
            s_of[0].append(math.log(omnipotent_fibo(i)))  
            s_of[1].append(math.log(perf_counter_ns() - t1)) 
    return s_of

def modify_fib():
    for _ in range(500):
        t1 = perf_counter_ns()
        s_fib = [],[]
        for i in range(10,50,5):
            s_fib[0].append(math.log(fib(i)))
            s_fib[1].append(math.log(perf_counter_ns() - t1))
    return s_fib

def modify_fib_Ala():
    for _ in range(500):
        t1 = perf_counter_ns()
        s_fib_2 = [],[]
        for i in range(10,50,5):
            s_fib_2[0].append(math.log(fib_Ala(i)))
            s_fib_2[1].append(math.log(perf_counter_ns() - t1))
    return s_fib_2

def profile_builder():
    ix = 5
    for _ in random.sample(range(100), k=5):
        fig, ax = plt.subplots()
        ax.plot(modify_fast_fib()[0], modify_fast_fib()[1], 'g-', label='fib_Sam') 
        ax.plot(modify_omnipotent_fibo()[0], modify_omnipotent_fibo()[1], 'r-.', label='Omni_fibo_Bay')
        ax.plot(modify_fib()[0], modify_fib()[1], 'b:', label='fast_fib_Dha')
        ax.plot(modify_fib_Ala()[0], modify_fib_Ala()[1], 'y--', label='fib_Ala')
        
        for marking in modify_fast_fib()[0]: #vertical markings for x axis
            ax.axvline(marking, color='k', linestyle='--', alpha=0.2)
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator()) #auto add minor tickers
        plt.legend(loc='best')
        plt.xlabel("log(fibonacci values)")
        plt.ylabel("log(time)")
        plt.title("Execution time for 4 different fibonacci series")
        
        ix += 1
        savefile = 'fibonacci-plotter/fib_img' + str(ix) + '.png'  
        fig.savefig(savefile)  #save the 5 images
        plt.show()
        
        
if __name__ == "__main__":
    profile_builder()
    