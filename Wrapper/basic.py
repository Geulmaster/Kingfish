#conf = settings()

def manipulator(func):
    array = [32, 32, 3, 33,1] #temp!!!!!!!
    value = func(array)
    print(f"{func.__name__} is {value}")

if __name__ == "__main__":
    manipulator(min)