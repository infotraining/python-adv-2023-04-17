from collections import defaultdict, Counter, OrderedDict
from typing import List, Tuple

def tokenize_file(path: str) -> List[str]:
    with open(path, 'r') as file:
        words = [w.lower() for w in file.read().split()]
    return words

def get_most_common(words: List[str]) -> List[Tuple[int, str]]:
    """TODO"""

assert get_most_common(tokenize_file('holmes.txt')) == [(5704, 'the'), (2882, 'and'), (2756, 'of'), (2719, 'to'), (2648, 'a'), (2533, 'i'), (1757, 'in'), (1606, 'that'), (1370, 'was'), (1278, 'he')]