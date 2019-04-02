import operator
def person_lister(func):
    def inner(people):
        people = sorted(people, key=lambda l: int(l[2]))
        l = []
        for person in people:
            l.append(func(person))
        return l
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')