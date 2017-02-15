#import functions
from numpy import loadtxt
from pylab import imshow,show
#import data, then plot, then show
data=loadtxt("C:\\Users\\Aureliano\\Desktop\\stm.txt",float)
imshow(data,origin="lower")
show()
