class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        answer=""
        word1ptr=0
        word2ptr=0
        
        while(True):
            if word1ptr < len(word1):
                answer += word1[word1ptr]
                word1ptr+=1
            if word2ptr < len(word2):
                answer += word2[word2ptr]
                word2ptr+=1
            if word1ptr >= len(word1) and  word2ptr >= len(word2):
                break
        return answer
        