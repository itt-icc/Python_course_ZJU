def acronym(s):
    S=s.split()
    result=[]
    for i in S:
        result.append(i[0].upper())
    return "".join(result)

phrase=input()
print(acronym(phrase))