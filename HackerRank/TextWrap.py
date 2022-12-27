import textwrap

def wrap(string, max_width):
    wrapped=textwrap.wrap(string,max_width)
    return ('\n'.join(wrapped))
    
 

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)