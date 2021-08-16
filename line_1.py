from matplotlib import pyplot as plt
import numpy as np

def get_data():
    data = int(input('enter the number to be encoded in decimal:\n'))
    choise = input('enter your choise\n 1.unipolar\n 2.polar\n 3.bipolar\n 4.all\n')
    if choise == 'unipolar' or choise=='1':
        unipolar(data, show=True)
    elif choise == 'polar' or choise=='2':
        c2 = input('enter your choise\n 1.polar_NRZ\n 2.polar_RZ\n 3.polar_biphase\n')
        if c2 == 'polar_NRZ' or c2=='1':
            polar_NRZ(data, show=True)
        elif c2 == 'polar_RZ' or c2=='2':
            polar_RZ(data, show=True)
        elif c2 == 'polar_biphase' or c2=='3':
            polar_biphase(data, show=True)

    elif choise == 'bipolar' or choise=='3':
        bipolar(data, show=True)
    elif choise == 'all' or choise=='4':
        unipolar(data)
        polar_NRZ(data)
        polar_RZ(data)
        polar_biphase(data)
        bipolar(data)
        plt.show()

    else:
        print('choose values correctly')

def unipolar(data, show=False):
    z = bin(data)
    y=[]
    for i in z[2:]:
        y.append(int(i))
    y.append(y[-1])
    x = list(range(len(y)))
    print(z,y)
    plot(x,y)
    #plt.xscale('linear')
    plt.title('unipolar')
    if show:
        plt.show()
    return None

def polar_NRZ(data, show=False):
    z = bin(data)
    y1=[]
    for i in z[2:]:
        if i == '1':
            y1.append(-1)
        elif i=='0':
            y1.append(1)
    y2=[]
    if z[2]=='1':
        y2.append(-1)
    else:
        y2.append(1)
    for i in z[3:]:
        if i=='0':
            y2.append(y2[-1])
        elif i == '1':
            if y2[-1] == 1:
                y2.append(-1)
            else:
                y2.append(1)
    y1.append(y1[-1])
    y2.append(y2[-1])
    x = list(range(len(y1)))
    print(z,y1,y2)
    plt.figure(2)
    plot(x,y1)
    plt.title('polar_NRZ_L')
    plt.figure(3)
    plot(x,y2)
    plt.title('polar_NRZ_I')
    if show:
        plt.show()
    return None

def polar_RZ(data, show=False):
    z=bin(data)
    y=[]
    for i in z[2:]:
        if i=='0':
            y.append(-1)
            y.append(0)
        elif i=='1':
            y.append(1)
            y.append(0)
    # x = list(range(0,len(y),0.5))
    y.append(y[-1])
    x = np.arange(0,len(y)/2,.5)
    print(z,y)
    plt.figure(4)
    plot_1(x,y)
    plt.title('polar_RZ')
    if show:
        plt.show()

    return None

def polar_biphase(data, show=False):
    z = bin(data)
    y=[]
    for i in z[2:]:
        if i=='0':
            y.append(1)
            y.append(-1)
        elif i=='1':
            y.append(-1)
            y.append(1)
    y1=[]
    if z[2]=='1':
        y1.append(-1)
        y1.append(1)
    elif z[2]=='0':
        y1.append(1)
        y1.append(-1)
    for i in z[3:]:
        if i =='1':
            if y1[-1]==1:
                y1.append(1)
                y1.append(-1)
            elif y1[-1]==-1:
                y1.append(-1)
                y1.append(1)
        elif i=='0':
            y1.append(y1[-2])
            y1.append((y1[-2]))
    y.append(y[-1])
    y1.append(y1[-1])
    x = np.arange(0,len(y)/2,.5)
    plt.figure(5)
    plot_1(x,y)
    plt.title('polar_biphase_manchester')
    plt.figure(6)
    plot_1(x,y1)
    plt.title('polar_biphase_differential manchester')
    if show:
        plt.show()

    return None

def bipolar(data, show=False):
    z = bin(data)
    y=[]
    if z[2]=='1':
        y.append(1)
    else:
        y.append(0)
    for i in z[3:]:
        if i == '0':
            y.append(0)
        elif i=='1':
            for j in y[::-1]:
                if j == 1:
                    y.append(-1)
                    break
                elif j == -1:
                    y.append(1)
                    break
                elif 1 not in y:
                    y.append(1)
                    break
                else:
                    pass

    y1 = []
    if z[2]=='0':
        y1.append(1)
    else:
        y1.append(0)
    for i in z[3:]:
        if i=='1':
            y1.append(0)
        elif i=='0':
            for j in y1[::-1]:
                if j == 1:
                    y1.append(-1)
                    break
                elif j == -1:
                    y1.append(1)
                    break
                elif 1 not in y1:
                    y1.append(1)
                else:
                    pass

    y.append(y[-1])
    y1.append(y1[-1])
    x = list(range(len(y)))
    # x1 = list(range(len(y1)))
    print(z,y,y1)
    plt.figure(7)
    plot(x,y)
    plt.title('bipolar_AMI')
    plt.figure(8)
    plot(x,y1)
    plt.title('bipolar_pseodoternary')
    if show:
        plt.show()
    return None

def plot(x,y):
    y1=[]
    for i in range(len(x)):
        y1.append(2.5)
        y1.append(2)
    plt.step(x, y, where='post', label='bits')
    plt.vlines(x, -2, 2 ,colors='r',linestyles='dashed')
    plt.hlines(0, 0, len(x), linestyles='dashed')
    plt.step(np.arange(0,len(y1)/2,.5),y1,where='post',label='clock')
    plt.ylim(-3, 3)
    plt.xlim(0, len(x))
    plt.legend()
    return None

def plot_1(x,y):
    y1 = []
    for i in range(len(x)):
        y1.append(2.5)
        y1.append(2)
    plt.step(x, y, where='post', label='bits')
    plt.vlines([range(len(x))], -2, 2, colors='r', linestyles='dashed')
    plt.hlines(0, 0, len(x), linestyles='dashed')
    plt.step(np.arange(0, len(y1) / 2, .5), y1, where='post', label='clock')
    plt.ylim(-3, 3)
    plt.xlim(0, len(x) // 2)
    plt.legend()
    return None

if __name__ == '__main__':
    get_data()
