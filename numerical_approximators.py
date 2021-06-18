from termcolor import colored


class ODE():
    """ ODE approximation methods | pass a function"""
    def __init__(self,F):
        print("=======Initialising ODE approximation methods===========")
        global h
        h=1
        self.function = F
        self.method_list = print('Method list\n-euler(x,y)\n-huen(x,y)\n-modified_euler(x,y)')
        pass

    def euler(self,X:list, Y:list):
        """ Euler approximation method"""
        F = self.function
        for key in range(len(X)):
            if key==0:
                result = Y[0]
            else:
                result = Y[key-1] + h*F(X[key-1],Y[key-1])
                Y[key]=result
        return Y

    def huen(self, X:list, Y:list):
        """ Huen approximation method"""
        F = self.function
        Y_eul = self.euler(X,Y)
        for key in range(len(X)):
            if key==0:
                result = Y[0]
            else:
                result = Y[key-1] + (h/2)* (F(X[key-1],Y[key-1]) + F(X[key],Y_eul[key]))
                Y[key]= result
        return Y

    def __half_euler(self,X:list,Y:list,F,key):
        temp = Y[key-1] + h/2*F(X[key-1],Y[key-1])
        result = F((X[key-1]+X[key])/2,temp)
        return result

    def modified_euler(self, X:list, Y:list):
        """ Modified euler approximation method"""
        F = self.function
        for key in range(len(X)):
            if key==0:
                result = Y[0]
            else:
                half= self.__half_euler(X,Y,F,key)
                result = Y[key-1] + h* half
                Y[key]=result
        return Y 

class integral():
    def __init__(self,F):
        self.function = F
        print(f"=============Initialising integral approximation methods=============")
        pass

    def trapezoid(self,start,end):
        F = self.function
        h = end - start
        result = (h/2)*(F(start)+F(end))
        return result
    
    def composite_trapezoid(self,start,end,steps):
        F = self.function
        h = (end - start)/steps
        f_sum = 0
        for i in range(1,steps):
            f_sum += F(start+i*h)
        result = (h/2) * (F(start)+F(end)+2*f_sum)
        return result
    
    def simpsons(self,start,end):
        F = self.function
        h = (end - start)/2
        result = h/3* (F(start)+F(end)+4*F((end-start)/2))
        return result
    
    def composite_simpsons(self,start,end,steps):
        F = self.function
        h = (end - start)/steps
        f_sum_odd = 0
        f_sum_even = 0
        for i in range(1,steps):
            if i%2 == 0:
                f_sum_even += F(start+i*h)
            else:
                f_sum_odd += F(start+i*h)
        result = h/3* (F(start)+F(end)+4*f_sum_odd + 2*f_sum_even)
        return result
    
    def romberg(self,start,end,k,n,cache:dict):
        key = (k,n)
        if key in cache:
            return cache[key]
        if k==0:
            result = self.composite_trapezoid(start,end,n)
            cache[key] = result
            return result
        y_less = self.romberg(start,end,k-1,n,cache)
        y_more = self.romberg(start,end,k-1,n*2,cache)
        result= (pow(4,k)*y_more-y_less)/(pow(4,k)-1)
        cache[key]= result
        return result