#bubble sort

def bub_sort_kth_smallest(a,k):
    for i in range(0,k):
        for j in range(0,len(a)-1-i):
            if a[j+1]<a[j]:
                a[j],a[j+1] = a[j+1],a[j]

a = []
print("Enter 5 elements into an array:")
for i in range(0,5):
    t = int(input())
    a.append(t)
    
k = int(input("Enter the value of k:"))

bub_sort_kth_smallest(a,k)
