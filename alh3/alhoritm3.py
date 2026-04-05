from alhoritm22.alhoritm22 import Generator
from alhoritm22.alhoritm22 import Outerwear
from alhoritm3.Abstr import AbstractStructureBasic, AbstractStructureExtended
from Strexampl import StructureExample

g = Generator()
g5 = [g.generate_single() for i in range(5)]
lst = g5
print (lst)

tpl = tuple (g5)
print (tpl)

s1 = StructureExample(lst)
print(s1.__repr__())