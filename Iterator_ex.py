""" mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit)) """


class Mynumbers:
    def __iter__(self):
        self.a=1
        print("Initialize")
        return self
    def __next__(self):
        print("*****"+self)
        if self.a < 20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myn=Mynumbers()
for x in iter(myn):
    print(x)