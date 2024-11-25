class ProcessTestData:
  def __init__(self, data) -> None:
    self.data =data
    


  def imputerFrTest(self):
    self.data  = self.data[0]
    for i in range(len(self.data)):
      if i<2:
        continue
      

      elif i==3:
        if self.data[i] =='female':
          self.data[i] = 0.797
        else:
          self.data[i] = 0.203

      elif i==6:
        if self.data[i] =='o':
          self.data[i] = 0.063
        elif self.data[i] =='C':
          self.data[i] = 0.125
        elif self.data[i] =='E':
          self.data[i] = 0.159
        elif self.data[i] =='G':
          self.data[i] = 0.106
        elif self.data[i] =='D':
          self.data[i] = 0.160
        elif self.data[i] =='A':
          self.data[i] = 0.099
        elif self.data[i] =='B':
          self.data[i] = 0.156
        elif self.data[i] =='F':
          self.data[i] = 0.130
        
        else:
          self.data[i] = 0.0001

      elif i==7:
        if self.data[i] =='S':
          self.data[i] = 0.262
        elif self.data[i] =='C':
          self.data[i] = 0.435
        else:
          self.data[i] = 0.303

    return self.data
  


