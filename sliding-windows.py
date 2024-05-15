
# is a number odd? use mod

# move the window over the array
    # loop over the window
        # check to see if everything from 1 index to another is odd

def even(x):
    ''' function to determine if number is even'''
    return x % 2 == 0

def sliding_Window(arr, window_size):
    ''' function that uses a window that moves through
      array to determine if all numbers in window_size are odd '''
    
    all_odd = True

    for i in range(0, window_size):
        if even(arr[i]):
            all_odd = False

    print(all_odd)
