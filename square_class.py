
  ## Determine whether list is uniquw
def isUnique(ls):
  return len(ls)==len(set(ls))


class Square:
  ## initiae class
  def __init__ (self, positions):
    self.positions = positions
  
  ## Determine if rows are unique  
  def rowsUnique(self):
    
    ## Get Positions
    r1ls = self.positions[0,1]
    r2ls = self.positions[2,3]
    
    
    ## Determine if unique
    r1 = len(r1ls)==len(set(r1ls))
    r2 = len(r2ls)==len(set(r2ls))
    
    
    return ([r1, r2])
  
  
  
  ## Determine if columns are unique
  def colsUnique(self):
    c1 = isUnique(self.positions[0,2])
    c2 = isUnique(self.positions[1,3])
    return [c1, c2]
  ## Determine if square is unique
  def squareUnique(self):
    square = isUnique(self.positions[0,1,2,3])
    return square
  
  ## Print Square Value
  def printList(self):
    return self.positions



tlSquare = Square([1,2,4,4])

print(tlSquare.printList())


print(tlSquare.rowsUnique)
