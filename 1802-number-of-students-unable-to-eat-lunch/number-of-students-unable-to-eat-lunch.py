class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        count=len(students)
        while students and i<len(students):
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count-=1
                i=0
            else:
                students.append(students.pop(0))
                i+=1
        return count
        