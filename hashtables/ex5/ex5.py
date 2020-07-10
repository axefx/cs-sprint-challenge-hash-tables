# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = dict()
    result = []
    # set keys as filenames with list of file path as value
    for file in files:
        path = file.split("/")
        filename = path[-1]
        # handle if not in cache
        if filename not in cache:
            cache[filename] = []

        cache[filename].append(file)
    for q in queries:
        if q in cache:
            result += (cache[q])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
