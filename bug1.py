class Base:
# TODO: there's code missing in one or more lines below
class Base:
    def __init__(self, x, y, size):
        self.x, self.y, self.size = x, y, size
    def shape(self): return "This is a shape"
    def draw(self): raise NotImplementedError

class Circle(Base):
def __init__(x, size):
super().__init__(x, y, size)
def draw(self):
return f"""
({self.x}, {self.y})\n{self.size}
	 , - ~ ~ ~ - ,
        '             '
      ,                 ,
     ,                   ,
    ,                     ,
   ,		           ,
   ,                       , 
   ,                       ,
    ,                     ,
     ,                   ,
      ,                ,
       ' - , _ _ _ , '
              """

def main():
    c = Circle(1,2,3)
    print(c.shape())
    print(c.draw())

if __name__ == "__main__":
    main()