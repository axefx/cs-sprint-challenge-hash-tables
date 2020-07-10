def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = dict()
    result = []
    arr_count = 0
    for arr in arrays:
        arr_count += 1
        for i in arr:
            if i not in cache:
                cache[i] = 0

            cache[i] +=1
    for i in cache:
        if cache[i] == arr_count:
            result.append(i)
    return result


if __name__ == "__main__":
    arrays = []
    arrays = [
            [1,2,3],
            [1,4,5],
            [1,6,7]
        ]
    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
