
liste=[[1, 2], [3, 4], [5, 6, 7]]
reverse_list=[]


def reverse(liste):
    lista=[]
    for item in liste[::-1]:
      if isinstance(item,list):
        reverse(item)
      else:
         lista.append(item)
    reverse_list.append(lista)
  


reverse(liste)
del reverse_list[-1] 
print(reverse_list)