import operator

class Scientist(object):
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    def __repr__(self):
        return self.name + ' : ' + str(self.birth)

scientists = [
    Scientist('Alan Guth', 1947),
    Scientist('Brian Schmidt', 1967),
    Scientist('Brian Greene', 1963),
    Scientist('Lawrence Krauss', 1954),
    Scientist('Frank Wilczek', 1951),
    Scientist('David Gross', 1941),
    Scientist('Wendy Freedman', 1957),
    Scientist('Maria Spiropulu',1970),
    Scientist('George Smoot III', 1945),
    Scientist('Saul Perlmutter', 1959)
]

for s in scientists:
    print(s)
print('-'*30)

for s in sorted(scientists, key=operator.attrgetter('name')):
    print(s)
print('-'*30)

for s in sorted(scientists, key=operator.attrgetter('birth')):
    print(s)
print('-'*30) 
