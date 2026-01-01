import cProfile
import pstats
from io import StringIO
import numpy as np

def compute_heavy_task(data):
    # Use numpy for efficient computation
    arr = np.array(data)
    result = np.sum(arr ** 2)
    return result

def main():
    # Lazy loading large data
    def load_data():
        # Simulate loading large data only when needed
        return list(range(1000000))
    data = load_data()
    output = compute_heavy_task(data)
    print(f'Result: {output}')

if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    main()
    pr.disable()
    s = StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats(10)
    print(s.getvalue())
