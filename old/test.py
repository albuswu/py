from multiprocessing import Process, Pool
#import testx

import subprocess, sys

##p =  Process(target=testx.haha)
##p.strat()
##p.join()

##def f(x):
##    return x*x
##
##if __name__ == '__main__':
##    p = Pool(3)
##    print(p.map(f,[1,2,3]))

##def f(name):
##    print 'hello',name
##
##if __name__ == '__main__':
##    p = Process(target=f, args=('bob',))
##    p.start()
##    p.join()

subprocess.Popen([sys.executable, "testxxx.py"])
print "end"
