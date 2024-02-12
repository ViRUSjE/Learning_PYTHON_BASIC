"Combining list"
myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

"""The function combines a list using spaces

:param myList: A list of strings
:rtype: string
:return: combined list
"""
def join_string(list):
    connected_string = ' '.join(list)
    return connected_string

connected_string = join_string(myList)
print(connected_string)
print(type(connected_string))
