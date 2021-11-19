from time import time

def timer(func):
    # define a function within a function, and call it with a decorator (@timer)
    # Takes any amount of arguments: args = arguments, kwargs = keyword arguments
    def wrapper(*args, **kwargs):
        start_time = time()
        print(f"\nTime required: {(time() - start_time)*1000:.2f} ms")
        result = func(*args, **kwargs)
        return result
    return wrapper

@timer
def get_volume(x,y,z,unit):
    vol = x * y * z
    print(f"Volume is {vol} {unit}³")
# get_volume = timer(get_volume)

if __name__ == "__main__":
    timer(get_volume)(3,4,5,"cm")
    get_volume(234,55,434,"mm")
    get_volume(5,5,5,"m")