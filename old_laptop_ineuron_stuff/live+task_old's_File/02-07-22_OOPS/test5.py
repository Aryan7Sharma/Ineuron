import logging

class Task5:
    logging.basicConfig(filename="list_class.log", level=logging.DEBUG, filemode="r+",
                        format='%(name)s - %(asctime)s %(levelname)s - %(message)s')
    log = logging.getLogger()
    log.info("Inside a List Class")

    # -1 Try to print a prime number in between 1 to 1000
    def check_isprime(self,n):
        for i in range(2, n):
            if n % i == 0: return False
        return True

    def prime(self,s,e):
        ans=[]
        for i in (s,e):
            if self.check_isprime(i):ans.append(i)

    # -2 Try to print a function which is eqivalent to print function in python:
    def Print(*a):
        return a

    # -3 Try to write a function which is a replicate of list append , extend and pop function.
    def append(List, val):
        List += [0]
        List[-1] = val
        return List

    def extend(List, val):
        List[len(List)::] = val[0::]
        return List

    def pop(List):
        pop = List[-1]
        List = List[0:-1]
        return pop, List

    # -4 Try to write a lambda function which can return a concatination of all the string that we will pass.
    #def concati(self,):
    #l = ["i", "N", "e", "u", "r", "o", "n"]

    #"".join(map(lambda x: x, l))


