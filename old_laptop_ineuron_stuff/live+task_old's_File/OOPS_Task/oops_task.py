'''
For this task i created a 10 different different classes and the some classes are connected with each other
In these 10 class I covered all the task topics like

class
object
constructor
inheritance
private
public
protected
abstraction
encaptulations
polymorpsim
package
modules
method overrridding



ans i did not use a single print statement instead a print i used a logging
ans i also use a exception handling so my code will work more sufficiently and  in a proper way

'''

import logging
logging.basicConfig(filename="class_1to10_logging.txt",level=logging.DEBUG,format='%(name)s - %(asctime)s - %(levelname)s - %(message)s')
logging=logging.getLogger()
logging.info("User run task.py file")

class Ineuron:
    logging.info("We entered in class Ineuron")
    try:
        def __init__(self): # Constructor
            self.all_course=["FSDA","FSDS","FSDE","FSWD","AIOPS"]
            logging.info('ALL Courses are stored in array and the reference of that array in a (all_courses) variable')
    except Exception as e:
        logging.info("Now im inside a Exception block")
        logging.exception(e)


class Ineuronstudent(Ineuron): # This class is inherited by Ineuron Class (#Inheritance)
    _stu_detail={} # Protected Variable
    logging.info("We have a _stu_detail variable which holds the reference of student enrolled details hashmap ")
    try:
        def enter_stu_detail(self,sid,sname,email,course_name,phone):
            if sid in self._stu_detail:
                logging.info("if condition is Ture")
                return "Student is already exist or course is not exists yet"
            else:
                logging.info("IF condition is False so we are in else block that means student did not exist in our database")
                if course_name not in self.all_course:
                    logging.info("Course did not exixt yet")
                else:
                    self._stu_detail=[sname,email,course_name,phone]
                    logging.info("Student details entered successfully")
    except Exception as e:
        logging.info("Now im inside a Exception block")
        logging.exception(e)

class Assignment:
    logging.info("Now im inside a Assignment Class")
    try:
        def score(self,t1,t2,t3):
            logging.info("now im inside a score function details are total_student=%s  --no_of_submission=%s  --no_of_student=%s",t1,t2,t3)
            __total_student=t1                            # Abstraction
            __assignment_marks=t2 # for each assignment
            __total_submission=t3 # total number of sumbmission overall

            score= __total_submission*__assignment_marks
            average_score= score//__total_student # average score of each student
            logging.info("Score = %s,Average_Score = %s",score,average_score)
            return "Score = %s,Average_Score = %s",score,average_score
    except Exception as e:
        logging.info("Now im inside a except block because score function is terminated")
        logging.exception(e)


class Quizzes(Assignment): # Inheritance
    logging.info("Now im inside a Quizzes Class")
    try:
        def score(self,t1,t2,t3): # METHOD Overriding (of parent class (Assignment)
            logging.info("now im inside a score function")
            ranker1=t1 # 1 st ranker student marks
            ranker2=t2 # 2 nd ranker student marks
            ranker3=t3 # 3 rd ranker student marks
            score=ranker1+ranker2+ranker3 # Total score of Rankers
            total_student=3
            average_score = score //total_student # Average score of Rankers
            logging.info("Score = %s,Average_Score = %s", score, average_score)
            return "Score = %s,Average_Score = %s", score, average_score
    except Exception as e:
        logging.info("Now im inside a except block because score function is terminated of Quizzes Class")
        logging.exception(e)

class Circulism:
    try:
        # IMPORTING circulism Module from syallus pakage
        import syallus.circulism as ci
        logging.info("circulism Module imported successfully")

        obj=ci.Circulism() # initializing the obj of (Circulism type)
        obj.show_content()
        logging.info("Result  --%s",obj.show_content())
    except Exception as e:
        logging.info("Now im inside a Exception Block")
        logging.info(e)

class One_neuron:
    logging.info("Now im inside a One_neuron Class")
    try:
        def __init__(self):
            self.__No_of_course=1000
            self.__Fees=7070
            self.__No_of_Students=25000
    except Exception as e:
        logging.info("Now im inside a Exception block")
        logging.exception(e)
    try:
        def show_details(self):#Data is Encapsulated means no one can be able to  modify that data without a help of proper method like setter
            logging.info("No_of_course = %s ,Fees = %s ,No_of_Students = %s",self.__No_of_course,self.__Fees,self.__No_of_Students)
            return "No_of_course = %s ,Fees = %s ,No_of_Students = %s".format(self.__No_of_course,self.__Fees,self.__No_of_Students)
    except Exception as e:
        logging.info("Now im inside a Exception Block")
        logging.exception(e)
    try:
        def modify_the_details(self,new_fees,new_coursess,new_students): # work as setter
            self.__Fees=new_fees
            self.__No_of_course+=new_coursess
            self.__No_of_Students+=new_students
            logging.info("No_of_course = %s ,Fees = %s ,No_of_Students = %s", self.__No_of_course, self.__Fees,self.__No_of_Students)
            return "No_of_course = %s ,Fees = %s ,No_of_Students = %s".format(self.__No_of_course, self.__Fees,self.__No_of_Students)
    except Exception as e:
        logging.info("Now im inside a Exception Block")
        logging.exception(e)


class Hall_of_Fame:
    logging.info("Now im inside a Hall of Fame class")
    __hashmap={} # private variable # abstraction
    try:
        def enter_details(self,**kwargs): # key is linkedin id and the value is all details in form of list
            logging.info("Now im inside a details method of hall of fame class")
            for k,v in kwargs.items():
                logging.info("%s == %s" % (k,v))
                self.__hashmap[k]=v
            return self.__hashmap
    except Exception as e:
        logging.info("now im inside a Exception Block")
        logging.exception(e)

class Information_of_HoF(Hall_of_Fame): # This class is inheriated by (hall of fame class) for seeing indivisual details
    logging.info("Now im inside a Information_of_HoF which is inheriated by (hall of fame class)")
    try:
        def show_info(self,*l_id):
            res=[]
            for i in l_id:
                logging.info("Person info %s",self._Hall_of_Fame__hashmap[i])
                res.append(self._Hall_of_Fame__hashmap[i])
            return res
    except Exception as e:
        logging.info("Now im inside a Exception Block")
        logging.exception(e)


#Polyforphism
class Duration: # polyforphism
    logging.info("now im inside a Duration Class")
    try:
        def __init__(self,branch):
            self.branch=branch
            logging.info("Branch == %s",self.branch)
    except Exception as e:
        logging.info("now im inside a Exception Block")
        logging.exception(e)
    try:
        def duration(self):
            if self.branch.lower()=="one neuron":
                dur= "Life Time"
            else:
                dur="Limited"
            logging.info("Duration = %s",dur)
            return dur
    except Exception as e:
        logging.info("now im inside a Except block")
        logging.exception(e)


# multiple constructor
class Enrolled:
    logging.info("now im inside a Enrolled Class") # one student can enrolled for min 1 couse and max 4 couse
    try:
        def __init__(self,*args):
            if len(args)==1:
                self.one=args[0]
                logging.info("%s",self.one)
            elif len(args)==2:
                self.one=args[0]
                self.two=args[1]
                logging.info("%s -- %s", self.one, self.two)
            elif len(args) == 3:
                self.one = args[0]
                self.two = args[1]
                self.three=args[2]
                logging.info("%s -- %s -- %s", self.one, self.two, self.three)
            elif len(args) == 4:
                self.one = args[0]
                self.two = args[1]
                self.three=args[2]
                self.four=args[3]
                logging.info("%s -- %s -- %s -- %s", self.one, self.two, self.three, self.four)
            logging.info("Excuted successfully")
    except Exception as e:
        logging.info("now im inside a except block")
        logging.exception(e)

obj=Enrolled("FSDS","ML")



