import inspect
from detector import calculate_midpoint

def assert_equal(actual = None, expected = None):
    caller = inspect.stack()[1][3]
    if actual == None or expected == None:
        print("ERROR: " + caller)
    elif actual == expected:
        print("\nPASS: " + caller)
    else:
        print("FAIL: expected " + str(actual) + " == " + str(expected))
        print("  in " + caller)

def test_calculate_midpoint():
    result = calculate_midpoint([[0, 0], [0, 1], [1, 0], [1, 1]])
    # assert result == 0.6 
    assert_equal(result, [0.5, 0.5])


if __name__ == "__main__":
    test_calculate_midpoint()
