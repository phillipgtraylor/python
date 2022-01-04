import converters

c1 = converters.ScaleConverter('inches', 'mm', 25)
print(c1.description())
print('Converting 23 inches')
print(str(c1.convert(23)) + c1.units_to)

c2 = converters.ScaleAndOffsetConverter('c', 'f', 1.8, 32)
print(c2.description())
print('Converting 2094C')
print(str(c2.convert(2094)) + c2.units_to)