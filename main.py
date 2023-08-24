class Solution:
    def expandAtCenter(self, string, left, right):
        while(left>=0 and right<len(string) and string[left]==string[right]):
            left-=1
            right+=1
            
        return right-left-1
        
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        if len(s)==0: return ""
        for i in range(len(s)):
            len1 = self.expandAtCenter(s, i, i)
            len2 = self.expandAtCenter(s, i, i+1)
            length = max(len1, len2)
            if length>(end-start):
                start = i - (length-1)//2
                end = i + length//2
            
        return s[start:end+1]
