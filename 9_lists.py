'''Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered and unindexed. No duplicate members.
    Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
'''

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])
thislist[1] = "blackcurrant"
print(thislist)

for x in thislist:
    print(x)
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")  

thislist.append("orange")
print(thislist)