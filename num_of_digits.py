
class Solution:
    def evenlyDivides (self, N):
        self.N = N
        num_list = list(str(N))
        divider_set = []
        for every_num in num_list:
            if int(every_num) == 0:
                pass
            else:
                if N % int(every_num) == 0:
                    if every_num not in divider_set:
                        divider_set.append(int(every_num))
                print(divider_set)
        return len(divider_set)
    
N = int(input('ENTER A NUMBER:'))
result = Solution()
print (result.evenlyDivides(N))