def divide_two(n):
    i=0
    if n<2:
        raise ValueError('value must be bigger than two')
    else:
        while n>=2:
            n=n//2
            print(n)
            i+= 1
    
    return i

if __name__ == "__main__":
    print(divide_two(int(input('input>> '))))