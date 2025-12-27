
from collections import defaultdict

x, y = map(int, input().split())
index_map = defaultdict(list)

for i in range(x):
    word = input()
    index_map[word].append(i + 1)
    
for _ in range(y):
    query_word = input()
    if query_word in index_map:
        indices = index_map[query_word]
        print(*indices) 
    else:
        print("-1")




