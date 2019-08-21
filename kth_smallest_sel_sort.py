#selection sort

def sel_sort_kth_smallest(a,k):
    for i in range(0,k):
        mini = i
        for j in range(i+1,len(a)):
            if a[j]<a[mini]:
                mini = j
        a[mini],a[i] = a[i],a[mini]
        
    return a[k-1]

        
a = []
print("Enter 5 elements into an array:")
for i in range(0,5):
    t = int(input())
    a.append(t)

k = int(input("VALUE OF K:"))
    

print(sel_sort_kth_smallest(a,k))

