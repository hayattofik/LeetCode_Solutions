def swap_case(s):
    output = ""
    for let in range(len(s)):
        
        if s[let] == " ":
            output += " "
            continue
        for i in range(len(s[let])):
            if s[let][i].lower() == s[let][i]:
                output+=s[let][i].upper()
            elif  s[let][i].upper() == s[let][i]:
                output+=s[let][i].lower()
            else:
                output +=str(s[let][i])
    return output
        

    
 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
