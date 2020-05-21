'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import math
def sliding_window_max(nums, k):
    window=[]
    result =[]
    append_index=0
    
    for i in range(len(nums)):
        for i in range(append_index,len(nums)):
            if len(window)<= (k-1):

                window.append(nums[i])
                append_index+=1
                print(append_index)
        print(window)
        result.append(max(window))
        if append_index!= len(nums):
            window.pop(0)
        else:
            break
        


    return result

            
            





if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
