class Vector:
    def __init__(self, coords):
        self.coords = list(coords)
    
    def __repr__(self):
        return f"Vector{self.coords}"
    
    def __len__(self):
        return len(self.coords)
    
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __getitem__(self,idx):
        return self.coords[idx]
    
    def __setitem__(self, idx, value):
        self.coords[idx] = value

    def __add__(self, other):
        return Vector([x + y for x,y in zip(self.coords, other.coords)])
    
    def __mul__(self, other):
        return Vector([other * x for x in self.coords])
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
