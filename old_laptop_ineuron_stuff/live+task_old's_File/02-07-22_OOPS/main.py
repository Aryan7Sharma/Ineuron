import logging
class List:
    logging.basicConfig(filename="list_class.log",level=logging.DEBUG,filemode="r+",format='%(name)s - %(asctime)s %(levelname)s - %(message)s')
    log=logging.getLogger()
    log.info("Inside a List Class")
    try:
        log.info("Now I am Inside a Try Block")
        def append(self,l,value):
            self.log.info("Now I am Inside a append Function")
            l+=value
            self.log.info(f"The output is %s",l)
            return l
        def extend(self,l,value): # It must that value should be iterables
            self.log.info("Now I am Inside a Extend Function")
            for i in value:
                l+=i
            self.log.info("The output is %s", l)
            return l

        def pow(self,l):
            self.log.info(f"Now I am Inside Pow Function and it excuted successfully and a class is --%s-- and the object name is --%s--", self.__class__.__name__,self.__str__())
            return [i*i for i in l]# it necessary to all elements of list is integer or float
    except Exception as e:
        log.info("Now I am Inside a Except Block")
        log.exception(e)
    #def __str__(self):
        #return "hello"
obj_oflist=List()
obj_oflist.extend([1,2,3],"abc")
obj_oflist.append([1,2,3],"abc")
obj_oflist.pow([1,2,3,4,5])
print(type(obj_oflist))
