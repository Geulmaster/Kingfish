from Wrapper import read_config

config = read_config()

array = config["VALUES_LIST"]

def manipulator(func):
    value = func(array)
    print(f"{func.__name__} is {value}")

if __name__ == "__main__":
    manipulator(min)