def count_words(seq, word_size):
    """Count subsequences (k-mers) in seq of given length
    """
    d = {}
    for i in range(0, len(seq)-word_size+1):
        word = seq[i:i+word_size]
        if word not in d:
            d[word] = 0
        d[word] += 1
    n = sum(d.values())
    for word in d:
        d[word] = [d[word], d[word] / n * 100]
    return d


def reverse(seq):
    d = {}
    for i in range(0,len(seq)):
        d[i]=seq[len(seq)-1-i]
    return d

def complement(seq):
    d={}
    s={'A':'T','T':'A','C':'G','G':'C'}
    for i in range(0,len(seq)):
        d[i]=s[seq[i]]
    return d
