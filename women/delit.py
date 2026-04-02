word = "Hello from python Russian"

ids = set()

for _ in range(100):
    word += str(_) 
    ids.add(id(word))
    
print(len(ids))