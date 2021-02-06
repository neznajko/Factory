#! /usr/bin/env python3
################################################################
jobs_time = [0,0,0,0,0]
# ]:(-
class Mach:
  # 
  def __init__(self, delay):
    self.delay = delay
    self.time  = [0] * len(delay)
  #  
  def assign_job(self, j):
    ## update machine times
    for i in range(len(self.time)):
      if self.time[i] < jobs_time[j]:
        self.time[i] = jobs_time[j]
    total = [x + y for (x, y) in zip(self.delay, self.time)]
    m = total.index(min(total))
    jobs_time[j] = self.time[m] = total[m]
# =g)    
if __name__ == '__main__':
  if 1: import pdb; pdb.set_trace()
  amach = Mach((1, 2))
  for j in range(len(jobs_time)):
    amach.assign_job(j)
  print(jobs_time[-1])
  # %;"
  bmach = Mach((1, 2, 4))
  for j in range(len(jobs_time)):
    bmach.assign_job(j)
  print(jobs_time[-1])
  # .(:o
################################################################
# log: - Naming someone bad won't make you good,.
