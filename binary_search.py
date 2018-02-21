##BINARY SEARCH
##
##runs on O(ln n)

def binary_search_rec(seq,key): # Recursive
    if not seq : return None
        mid = len(seq)//2
    if key == seq[mid] : return mid
    elif key < seq[mid] : return binary_search_rec(seq[:mid],key)
    else : return binary_search_rec(seq[mid+1:],key)
def binary_search_iter(seq,key): # Iterative
    hi, lo = len(seq), 0
    while lo < hi :
        mid = (hi + lo)//2
    if key == seq[mid] : return mid
    elif key < seq[mid] : hi = mid
    else : low = mid + 1
    return None
def test_binary_search():
    seq = [1,2,5,6,7,10,12,12,14,15]
    key = 6
    assert(binary_search_iter(seq, key) == 3)
    assert(binary_search_rec(seq, key) == 3)
    print('Tests passed!')
if __name__ == '__main__':
test_binary_search()
