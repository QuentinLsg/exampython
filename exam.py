import datetime, time
import queue
##ARRRIVER EN RETARD A 11H QUENTIN LESEIGNEUR
class Tank:
  def __init__(self):
    self.CAPACITY = 50
    self.STORAGE = 0
    self.FIFO = queue.Queue()

  def putOil(self, number):
    if self.STORAGE + number > self.CAPACITY:
      print("full tank")
    else:
      self.STORAGE += number

  def sendOil(self, number):
    print("Send" + str(self.STORAGE))
    self.STORAGE -= number

class Pump:

  def __init__(self, NAME, IS_INTERRUPTIBLE, PERIOD, EXECUTION_TIME, PRODUCTION, PRIORITY = 0) :
    self.NAME = NAME
    self.IS_INTERRUPTIBLE = IS_INTERRUPTIBLE
    self.PERIOD = PERIOD
    self.EXECUTION_TIME = EXECUTION_TIME
    self.PRODUCTION = PRODUCTION

    self.PRIORITY = PRIORITY		# 0 by default

    self.NEXT_DEADLINE = datetime.datetime.now()
    self.LAST_EXECUTED_TIME = datetime.datetime.now()

    if self.IS_INTERRUPTIBLE == True :
      self.EXECUTION_DONE = 0		
    else :
      self.EXECUTION_DONE = 100		# Big number by default


  def need_to_run(self):
    return True
    

  def run(self):

    global timer
    if self.IS_INTERRUPTIBLE == False :
      print(self.NAME + "send :" + str(self.PRODUCTION) + "oils")
      tank.putOil(self.PRODUCTION)
      tank.sendOil(self.PRODUCTION)
      time.sleep(self.EXECUTION_TIME)
      self.NEXT_DEADLINE = self.NEXT_DEADLINE + datetime.timedelta(seconds=self.PERIOD)


class Machine:

  def __init__(self, NAME, IS_INTERRUPTIBLE, PERIOD, EXECUTION_TIME, PRODUCTION, TYPE, PRIORITY = 0) :
    self.NAME = NAME
    self.IS_INTERRUPTIBLE = IS_INTERRUPTIBLE
    self.PERIOD = PERIOD
    self.EXECUTION_TIME = EXECUTION_TIME
    self.PRODUCTION = PRODUCTION
    self.TYPE = TYPE
    self.STOCKAGE = 30

    self.PRIORITY = PRIORITY		# 0 by default

    self.NEXT_DEADLINE = datetime.datetime.now()
    self.LAST_EXECUTED_TIME = datetime.datetime.now()

    if self.IS_INTERRUPTIBLE == True :
      self.EXECUTION_DONE = 0
    else :
      self.EXECUTION_DONE = 100		# Big number by default


  def need_to_run(self):
    return True

  def addoil(self, number):
    self.STOCKAGE += number


  def run(self):

    global timer
    if self.IS_INTERRUPTIBLE == False :
      if self.STOCKAGE >= self.PRODUCTION:
        print(self.NAME + "use :" + str(self.PRODUCTION) + "oils to create a " + self.TYPE)
        self.STOCKAGE -= self.PRODUCTION
        time.sleep(self.EXECUTION_TIME)
        self.NEXT_DEADLINE = self.NEXT_DEADLINE + datetime.timedelta(seconds=self.PERIOD)
      else:
        print("Not Enough oil")





if __name__ == "__main__":

  print("aer")
    # Definition of all tasks and instanciation
  pump_list  = [ 
    Pump(NAME = 'Pump 1', IS_INTERRUPTIBLE = False, PERIOD = 5, EXECUTION_TIME = 2, PRODUCTION = 10),
    Pump(NAME = 'Pump 2', IS_INTERRUPTIBLE = False, PERIOD =  15, EXECUTION_TIME = 3, PRODUCTION = 20),
    Machine(NAME = 'Machine 1', IS_INTERRUPTIBLE = False, PERIOD = 5, EXECUTION_TIME = 5, PRODUCTION = 25, TYPE = "Motor"),
    Machine(NAME = 'Machine 2', IS_INTERRUPTIBLE = False, PERIOD = 5, EXECUTION_TIME = 3  , PRODUCTION = 5, TYPE = "Wheel")
]
  tank = Tank()
  global timer
  timer = -1

  while(True):
    timer +=1

    task_to_run = None
    task_priority = 0
    timer += 1

    for current_task in pump_list  :

      current_task_need_to_run = current_task.need_to_run()

      task_to_run = current_task
      task_to_run.run()

