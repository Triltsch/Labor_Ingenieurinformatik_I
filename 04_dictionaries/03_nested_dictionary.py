"""
 Ein anderes Beispiel für Dictionary im Dictionary (nested)
 hier sind die keys Zahlen

@created: 02.11.2022
@author: U.Triltsch
"""

digits = {1: {'Word': 'one', 'Roman': 'I'},
          2: {'Word': 'two', 'Roman': 'II'},
          3: {'Word': 'three', 'Roman': 'III'},
          4: {'Word': 'four', 'Roman': 'IV'},
          5: {'Word': 'five', 'Roman': 'V'}}

print(digits[1]['Word'])
print(digits[4]['Roman'])
