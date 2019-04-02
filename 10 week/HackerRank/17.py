l = []

for _ in range(int(raw_input())):
    command = raw_input()
    
    if command[:6] == "append":
        l.append(int(command.split()[-1]))
    elif command[:6] == "insert":
        l.insert(int(command.split()[-2]), int(command.split()[-1]))
    elif command[:6] == "remove":
        l.remove(int(command.split()[-1]))
    elif command[:3] == "pop":
        l.pop()
    elif command[:5] == "index":
        l.index(int(command.split()[-1]))
    elif command[:5] == "count":
        l.count(int(command.split()[-1]))
    elif command[:4] == "sort":
        l.sort()
    elif command[:7] == "reverse":
        l.reverse()
    elif command[:5] == "print":
        print l 