
def linear_search(l:list, target:int) -> int:
    for i in range(len(l)):
        if l[i] == target:
            return i