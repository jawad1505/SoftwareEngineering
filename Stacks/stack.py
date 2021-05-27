"""
Stack Data Structure.
"""
""" First in Last Out"""
class Stack():
    def __init__(self) -> None:
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items

if __name__ == '__main__':
    st = Stack()
    st.push("A")        # add at end
    st.push("B")
    st.push("C")
    st.push("D")
    print(st.get_stack())
    print()
    print(st.pop())      # delete last element
    print(st.get_stack())
    print(st.is_empty()) # check
    print(st.peek())     # get last element

