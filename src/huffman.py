# from itertools import batched # TO-DO: fix not working with current python version, +3.12 needed

import queue

def batched_manual(iterable, n):
    # A simple manual implementation of batched
    if n < 1:
        raise ValueError('n must be at least one')
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == n:
            yield tuple(batch)
            batch = []
    if batch:
        yield tuple(batch)

def build_huffman_tree(imarray, n=1):
    # Count element frequencies
    element_counts = {}
    for element in batched_manual(imarray.flatten(), n):
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    # Build priority queue to apply Huffman algorithm
    id = {}
    idr = {}
    q = queue.PriorityQueue()
    for key, value in element_counts.items():
        print(f"{key}, ")
        id[key] = len(id)
        idr[id[key]] = key
        q.put((value, [id[key]]))

    # Build Huffman tree (transf maps id to reversed code path)
    transf = {}
    while q.qsize() > 1:
        a = q.get()
        b = q.get()
        for i in a[1]:
            if i in transf:
                transf[i] += '1'
            else:
                transf[i] = '1'
        for i in b[1]:
            if i in transf:
                transf[i] += '0'
            else:
                transf[i] = '0'
        new_val = (a[0] + b[0], a[1] + b[1])
        q.put(new_val)

    # Reverse Huffman tree paths to get actual codes (transf maps id to code)
    for key, path in transf.items():
        transf[key] = path[::-1]

    # Build decoding dictionary mapping code string to original pixel tuple
    code_to_pixel_tuple = {}
    # Assuming 'id' maps pixel tuples to element IDs, and 'transf' maps element IDs to codes
    for pixel_tuple, element_id in id.items():
         code = transf[element_id]
         code_to_pixel_tuple[code] = pixel_tuple

    return transf, id, idr, code_to_pixel_tuple