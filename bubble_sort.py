def bubble_sort(list_num):
    for num in list_num:
        num_index = list_num.index(num)
        for i in range(0, len(list_num)):
                stored_val = list_num[i]
                if num_index > i:
                    if list_num[num_index] < list_num[i]:
                        list_num[i] = list_num[num_index]
                        list_num[num_index] = stored_val
                else:
                    if list_num[num_index] > list_num[i]:
                        list_num[i] = list_num[num_index]
                        list_num[num_index] = stored_val
    print(list_num)
bubble_sort(list_num=[5,2,3,1,4,6,3])