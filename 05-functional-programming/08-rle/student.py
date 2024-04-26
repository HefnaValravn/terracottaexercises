def rle_encode(data):
    data = iter(data)
    try:
        lastdatum = next(data)
        count = 1
        for datum in data:
            if datum == lastdatum:
                count += 1
            else:
                yield (lastdatum, count)
                lastdatum = datum
                count = 1
        yield (lastdatum, count)
    
    except StopIteration:
        pass



def rle_decode(data):
    for datum, count in data:
        for _ in range(count):
            yield datum