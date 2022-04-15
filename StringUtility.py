class StringUtility:
  
 def __init__(self,string):
  self.string = string

 def __str__(self):
  return "StringUtility"

 def vowels(self):
  a = "a"
  A = "A"
  e = "e"
  E = "E"
  i = "i"
  I = "I"
  o = "o"
  O = "O"
  u = "u"
  U = "U"
  acount = 0
  ecount = 0
  icount = 0
  ocount = 0
  ucount = 0
  if a or A in str:
     acount = acount + 1
  if E or e in str:
     ecount = ecount + 1
  if I or i in str:
    icount = icount + 1
  if o or O in str:
     ocount = ocount + 1
  if u or U in str:
     ucount = ucount + 1
 
 def bothEnds(self):
  if len(str) < 2:
   return ''
  return str[0:2] + str[-2:]

 def fixStart(self):
   return str[0]+str[1:].replace(str[0], '*')

 def asciiSum(self, n):
  sum = 0
  for i in range(n) :
        if (self(i + 1)):
            sum += ord(str[i]);
  return sum;

 def cipher(self):
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  cipher = ""
  for i in self.string:
    if i.isalpha():
      alphabet = ord(i) + len(self.string)
      if alphabet > ord("z"):
        alphabet = 26
      letter = chr(alphabet)
      cipher += letter
    