##################################
#bogo sort
# ritesh jayant
##################################

import random

def bogo_sort(list_):
  while not is_sorted(list_):
    random.shuffle(list_)
  return list_

def is_sorted(list_):
  for i in range(len(list_) - 1):
    if list_[i] > list_[i + 1]:
      return False
  return True


my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_list = bogo_sort(my_list)
print(sorted_list)

