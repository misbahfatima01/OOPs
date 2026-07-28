class DimensionalVector:
    def __init__(self, d):
       
        self._coords = [0] * d 
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, j):
        return self._coords[j]
    
    def __setitem__(self, j, value):
        self._coords[j] = value
        
    def __add__(self, other):     
      result = DimensionalVector(len(self)) 
      for i in range(len(self)):
            result[i] = self[i] + other[i]
      return result 
    
    def __eq__(self, other):
        return self._coords == other.coords
   
    def __str__(self):
        return str(self._coords)  
        