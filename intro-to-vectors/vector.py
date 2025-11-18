class Vector:
    def __init__(self, *coords):
        self.coords = tuple(coords)
    
    def __repr__(self):
        return f"Vector{self.coords}"
    
    def __len__(self):
        return len(self.coords)
    
    def __eq__(self, other):
        return self.coords == other.coords