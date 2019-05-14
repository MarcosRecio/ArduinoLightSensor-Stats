# import serial.tools.list_ports
# comlist = serial.tools.list_ports.comports()
# connected = []
# for element in comlist:
#     connected.append(element.device)
#     print("Connected COM ports: " + str(connected))



from serial import Serial
# import time
#import collections
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
def mean(*args):
    m = 0
    for i in args:
        m += i
    m /= len(args)
    return m

def mean_t(args):
    m = 0
    for i in args:
        m += i # m = m + i
    m /= len(args) # m = m/len(args)
    return m

def median(l):
    l = sorted (l, key = lambda x: x)
    if len(l)%2==0:
        return mean(l[len(l)//2-1],l[(len(l)//2)])
    else:
        return l[len(l)//2]
    
def deviation(v, measure):
    v -= mean_t(measure)
    return v

def typical_deviation(args):
    l = []
    for i in args:
         l.append(deviation(i,args))
    return mean_t(l)


def main():    
        
    port = '/dev/ttyACM0' # for mac '/dev/cu.usbmodem143301' # for Windows 'COM1' or 'COM5' are frequent
    ard = Serial(port, 38400, timeout=5)
    values = [] #collections.deque([0]*100, maxlen = 100)
    collecting_data = True
    while collecting_data:
                
        msg = ard.readline()
        # msg.flush()
        #print(msg)
        value = float(msg)
        values.append(value)
        print("------------------------ ------------ ------------------")
        print('Value: ' + str(value))
        if len(values)>100:
            values.pop(0)
        print(values)
        print('Average value (Mean): ' + str(mean_t(values)))
        print('Median: '+ str(median(values)))
        print('Typical deviation: '+ str(typical_deviation(values)))
        print("------------------------ ------------ ------------------")
        
        

if __name__ == '__main__':
    main()