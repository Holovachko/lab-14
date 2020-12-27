import math as m

class TPrism:
    def __init__(self, n , a , h):
        self.n = n
        self.a = a
        self.h = h
    def s_base(self):
        if self.n == 3:
            return (m.sqrt(3)/4)*self.a**2
        if self.n == 4:
            return self.a**2
        else:
            return (self.n * self.a**2)/4*m.tan(m.degrees(180)/self.n)
    def v_prism(self):
        return self.s_base()*self.h


t = TPrism(3,4,5)
print(t.s_base())


class TPrism3(TPrism):
    def __add__(self, other):
        return self.v_prism() + other.v_prism()

class TPrism4(TPrism):
    def __add__(self, other):
        return self.s_base() + other.s_base()





t1 = TPrism3(3,5,1)
t2 = TPrism3(3,4,7)
print(t2+ t1)

t3 = TPrism4(4,2,7)
t4 = TPrism4(4,6,1)

print(t3+t4)
