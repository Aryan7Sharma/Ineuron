import logging
logging.basicConfig(filename="log.txt",level=logging.DEBUG,format='%(name)s - %(asctime)s - %(levelname)s - %(message)s')
logging=logging.getLogger()
logging.info("User run circulism.py file which is inside a syallus pakage")
class Circulism:
    logging.info("Now im inside a Circulism class")
    try:
        def __init__(self):
            self.FSDA=["Statistics","Python","SQL"]
            self.FSDS=["Statistics","Python","SQL","Machine Learning","Computer Vision","Deep Learning","NLP","Flask"]
            self.FSDE=["Mathematics","Python","Tableau","Power BI","Aws","Azure"]
            self.AIOPS=["Mathematics","Docker","Gibhub","Aws"]
    except Exception as e:
        logging.info("Now im inside a Except Block")
        logging.exception(e)
    try:
        def show_content(self):
            logging.info("NOw im inside a show_content function")
            logging.info("course syallus are   FSDA -- %s --,  FSDS -- %s --,  FSDE -- %s --,  AIOPS-- %s --  ",self.FSDA,self.FSDS,self.FSDE,self.AIOPS)
            return "course syallus are   FSDA -- {0} --,  FSDS -- {1} --,  FSDE -- {2} --,  AIOPS-- {3} --  ".format(self.FSDA,self.FSDS,self.FSDE,self.AIOPS)
    except Exception as e:
        logging.info("Now im inside a Exception block of show_content function")
        logging.exception(e)



obj=Circulism()
print(obj.show_content())



