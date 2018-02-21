##Merge sort divides the list in half to create two unsorted lists. These two
##unsorted lists are sorted and merged by continually calling the merge-sort
##algorithm, until you get a list of size 1. The algorithm is stable, as well as
##fast for large data sets. However, since it is not in-place, it requires much
##more memory than many other algorithms. The space complexity is O(n)
##for arrays and O(ln n) for linked lists2. The best, average, and worst case
##times are all O(n ln n)


O(log(n))

def merge_sort(seq):
    if len(seq) < 2 : return seq
        mid = len(seq)//2
        left, right = None, None
    if seq[:mid]: left = merge_sort([:mid])
    if seq[mid:]: right = merge_sort([mid:])
        return merge_n(left,right)
#O(2n)
def merge_2n(left, right):
    if not left or not right:
    return left or right
    result = []
while left and right :
    if left[-1] >= right[-1]:
        result.append(left.pop())
    else:
        result.append(right.pop())
        result.reversed()
    return (left or right) + result
#O(n)
def merge_n(left,right):
    if not left or not right:
        return left or right
        result = []
        i,j = 0,0
        while i < len(left) and j < len(right):
            if left[i] <= right[i]:
                result.append(left[i])
                i+=1
            else :
                result.append(right[j])
                j+=1
            if i < len(left) - 1 : result+=left[i:]
            elif j < len(right) - 1 : result += right[j:]
            return result
def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(merge_sort(seq) == sorted(seq))
    print('Tests passed!')
if __name__ == '__main__':
test_merge_sort()
