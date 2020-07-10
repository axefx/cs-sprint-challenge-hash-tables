def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = dict()
    result = []
    for i in a:
        if i != 0:
            cache[i] = True
            if -i in cache:
                result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
