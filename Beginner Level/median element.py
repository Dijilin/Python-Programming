def median(lst):
    m = len(lst)
    if m < 1:
            return None
    if m % 2 == 1:
            return sorted(lst)[m//2]
    else:
            return sum(sorted(lst)[m//2-1:m//2+1])/2.0
