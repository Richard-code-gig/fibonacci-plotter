from time import perf_counter_ns
import math
import functools
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
plt.rcParams["figure.figsize"] = (8, 4.7)

"""First we define a decorator function that can modifies any function that generate integer result to produce iterators
The execution time between generating the ith and ith + 1 values can be gotten and plotted against their respective values
The decorator was positively tested with factorial, fibonacci and taylor series. No limit in practice"""

class Decorate: 
    def function(func):
        @functools.wraps(func) #Just for debugging purpose
        def wrapper(*args, **kwargs):
            for _ in range(500):
                t1 = perf_counter_ns()
                s_ff = [],[]
                for x in args:  #Since dict objects can't be interpreted as integers, this won't decorate functions that cache values in dict
                    for b in range(5,x,5): #The two 5's are because one of the fibonacci functions we are to modify breaks for n < 3
                        s_ff[0].append(math.log(func(b))) 
                        s_ff[1].append(math.log(perf_counter_ns() - t1)) 
            return s_ff
        return wrapper 
    
    
class Profile:
    #Lets define some setters and getter
    #So, users can extend the profile builder below to plot arbitrary number of functions
    
    def setMarker(self, markers):
        self.__markers = markers 
                                  
    def getMarker(self):    
        return self.__markers  
        
    marker = property(getMarker, setMarker) #The property allows 
        
    def setColor(self, colors):
        self.__colors = colors
        
    def getColor(self):
        return self.__colors

    color = property(getColor, setColor)
        
    def setLabels(self, labels):
        self.__labels = labels
        
    def getLabels(self):
        return self.__labels

    label = property(getLabels, setLabels)

    def setLinestyle(self, linestyle):
        self.__linestyle = linestyle
        
    def getLinestyle(self):
        return self.__linestyle

    linestyle = property(getLinestyle, setLinestyle)


    def profile_builder(self,xlabel, ylabel, title, args, saver=None): #args is a list of values and execution time for all our fibonacci functions
        ix = 0
        fig, ax = plt.subplots()
        for i in range(len(args)):
            ax.plot(args[i][0],args[i][1],marker=next(self.marker),color=next(self.color),linestyle=next(self.linestyle),label=next(self.label))
                
        for marking in args[0][0]: #vertical markings for x axis
            plt.axvline(marking, color='k', linestyle='--', alpha=0.2)
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator()) #auto add minor tickers
        plt.legend(loc='best')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        
        if saver:
            for _ in range(5): #Must be same number passed to k in random.sample in main() of decorator.py file
                ix += 1
                savefile = saver + str(ix) + '.png'  
                fig.savefig(savefile)  #save the plotted images
        plt.show()