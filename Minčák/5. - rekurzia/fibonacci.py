

def fibonaci(idy):
    if idy <= 1:
        return idy
    else:
        return fibonaci(idy - 1) + fibonaci(idy - 2)
    
print(fibonaci(30))