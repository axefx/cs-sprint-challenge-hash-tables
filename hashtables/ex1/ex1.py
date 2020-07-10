def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # save weight value as key and index as value
    cache = dict()

    for i in range(length):
        weight = weights[i]
        # for each weight find the difference to the limit
        # save in cache
        difference = limit - weight
        if difference not in cache:
            cache[weight] = i
        else:
            # output: [ 3, 1 ]
            return [i,cache[difference]]
    return None

if __name__ == "__main__":
    # [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    indices = get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], length = 5, limit = 21)
    print(indices) # output: [ 3, 1 ]