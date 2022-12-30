class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salarySum=sum(salary[1:len(salary)-1])
        AverageSalary = salarySum/(len(salary)- 2)
        return AverageSalary
        
        