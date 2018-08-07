
a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

def in_array(array1, array2):
    return sorted(set(filter(lambda e1: any(e1 in e2 for e2 in a2),a1)))




    
