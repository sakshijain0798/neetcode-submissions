class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visistedSet=set()
        def dfs(crs):
            if crs in visistedSet:
                return False
            if preMap[crs] == []:
                return True
            
            visistedSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visistedSet.remove(crs)
            preMap[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True