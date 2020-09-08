class student:
    def __init__(self, name, s_id, **marks):
        self.name = name
        self.s_id= s_id
        for i, j in marks.items():
            setattr(self, i, j)
        
    def average(self):
        total = 0
        data = vars(self)
        for i in data.values():
            if type(i) is int:
                total += i
        average = total / (len(data.values()) - 2)
        return total, average
 





 


        
            
        

