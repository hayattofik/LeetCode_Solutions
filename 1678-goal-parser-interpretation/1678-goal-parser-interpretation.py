class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        output=""
        for letter in range(len(command)): 
            if command[letter] == "(":
                if command[letter +1]=='a':
                    output+='a'
                elif command[letter +1] == ')':
                    output+= 'o'
            elif command[letter]=='l':
                output+='l'
            elif command[letter] == 'G':
                output+='G'
            else:
                continue
        return output
                    
            