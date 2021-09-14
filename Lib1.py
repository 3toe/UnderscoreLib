# Let's recreate some common functions from js's "underscore" module:

class Underscore:
   def map(self, iterable, callback):
      for i in range(len(iterable)):
         iterable[i] = callback(iterable[i])
      return iterable
      
   def find(self, iterable, callback):
      for i in range(len(iterable)):
         if callback(iterable[i]):
            return iterable[i]

   def filter(self, iterable, callback):
      list = []
      for i in range(len(iterable)):
         if callback(iterable[i]):
            list.append(iterable[i])
      return list
   
   def filterList(self, iterable, callback):
      for i in range(len(iterable)):
         if i >= len(iterable):
            break
         if callback(iterable[i]) == False:
            iterable.pop(i)
      return iterable

   def reject(self, iterable, callback):
      for i in range(len(iterable)):
         if i >= len(iterable):
            break
         if callback(iterable[i]) == True:
            iterable.pop(i)
      return iterable
      # your code      

# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore

SquaresMap =_.map([1,2,3], lambda x: x*2) # should return [2,4,6]
MoreThan4 = _.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
Evenz = _.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
Evenz2 = _.filterList([1,2,3,4,5,6], lambda x: x%2==0) # done without creating a new list. should return [2,4,6]
Oddz =_.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]

print(SquaresMap, MoreThan4, Evenz, Evenz2, Oddz)