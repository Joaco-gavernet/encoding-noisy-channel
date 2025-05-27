from notebooks.general_utils import *


def build_huffman_tree(imarray, x=1):
    histogram = {}
    for element in batched(imarray.flatten(), x):
        if element in histogram:
            histogram[element] += 1
        else:
            histogram[element] = 1

    # Build priority queue to apply Huffman algorithm
    id = {}
    idr = {}
    q = queue.PriorityQueue()
    for key, value in histogram.items():
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
    tr = {} # Transform in reverse
    for pixel_tuple, element_id in id.items():
         code = transf[element_id]
         tr[code] = pixel_tuple

    cimarray = ''
    for element in batched(imarray.flatten(), x):
        cimarray += transf[id[element]]

    return cimarray, tr