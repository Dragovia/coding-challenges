class Solution(object):
   def longestCommonPrefix(self, strs):
      """
      :type strs: List[str]
      :rtype: str
      """
      if len(strs) == 0:
         return ""
      current = strs[0]
      #print(current)
      for i in range(1,len(strs)): # position 1 to length of strs
         temp = ""  #temp is empty
         if len(current) == 0:  #if the is no word in current break
            break
         for j in range(len(strs[i])):  # for the range of the length of words
            if j<len(current) and current[j] == strs[i][j]:
               print( strs[i][j])
               temp+=current[j]
            else:
               break
         current = temp
      return current
input_list = ["dog","racecar","car"]#["school","schedule","scotland"]
ob1 = Solution()
print(ob1.longestCommonPrefix(input_list))