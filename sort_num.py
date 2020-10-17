def bubble_sort(alist):
  counter = 1
  while counter != len(alist):
    for x in range(0, len(alist)-1):
        val = x + 1
        if alist[x] > alist[val]:
            alist.insert(x, alist[val])
            alist.pop(x+2)
        else:
            counter += 1
  print(alist)
  
    
    

bubble_sort()




