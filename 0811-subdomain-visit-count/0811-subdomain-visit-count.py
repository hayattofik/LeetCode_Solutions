class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        countdic=defaultdict(int)
        output = []
        
        for domain in cpdomains:
            domain = domain.split()
            visitNo=domain[0]
            site = domain[1]
            countdic[site] += int(visitNo)
            
            site= site.split('.')
            countdic[site[-1]] +=int(visitNo)
      
            if len(site) ==3:
                key = site[-2] + "." + site[-1]
                countdic[key] += int(visitNo)
               
        for key in countdic:
            output.append (str(countdic[key]) + " " + key)
        return output
            
                
                         
        
                
                
        