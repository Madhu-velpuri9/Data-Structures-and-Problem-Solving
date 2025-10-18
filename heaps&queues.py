import heapq
#minheap
A=[-4,3,5,0,2,12,9,8]
heapq.heapify(A)
print(A)
#insert to heap
heapq.heappush(A,6)
print(A)
#remove element from the heap
minn=heapq.heappop(A)
print(A,'removed min:',minn)
#heap sort
def heapsort(arr):
    heapq.heapify(arr)
    n=len(arr)
    new_list=[0]*n
    for i in range(n):
        min1=heapq.heappop(arr)
        new_list[i]=min1
    return new_list
print(heapsort([-4,3,5,0,2,12,9,8]))
#maxheap
B=[-4,3,5,0,2,12,9,8]

for i in range(len(B)):
    B[i] = -B[i]
    heapq.heapify(B)
print(B)
N=[]
for i in range(len(B)):
    M=-heapq.heappop(B)
    N.append(M)
print(N)

