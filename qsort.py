# quicksort a list
# (See hw1.pdf for requirements.)

# Shang Chun Lin : HW1
def quicksort(alist):
    # +++your code here+++
    def partition(alist,low,high):
        pivot = alist[high-1]
        mid = low
        for count in range(low,high-1):
            if alist[count] < pivot:
                alist[count],alist[mid] = alist[mid],alist[count]
                mid += 1
        alist[high-1],alist[mid] = alist[mid],alist[high-1]
        return mid

    def sort_range(low, high):
        if high - low <= 1: return
        mid = partition(alist,low,high)
        sort_range(low,mid)
        sort_range(mid+1,high)

    sort_range(0, len(alist))

if __name__ == "__main__":
    a = [1,3,5,2,9,6,7,5]
    b = [42]       # special singleton case 
    c = []         # special empty list case 
    quicksort(a)
    quicksort(b)
    quicksort(c)
    print(a)       # => [1,2,3,5,5,6,7,9]
    print(b)       # => [42]
    print(c)       # => [] 
