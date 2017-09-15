

class Tree:

    def __init__(self):
        pass
        self.branch_count = 0
        self.initiator = Branch(self.branch_count)
        self.variables = [self.initiator]
        self.constants = [Leaf(), Left(), Right()]
        self.rules = dict()
        self.age = 0
        self.state = [self.initiator]

    def add_branch_type(self):
        self.branch_count += 1
        branch = Branch(self.branch_count)
        self.variables.append(branch)
        return branch

    def add_generating_rule(self, initiator, consequence):
        if initiator not in self.variables:
            raise NotInAlphabetException()
        for e in consequence:
            if e not in self.variables and e not in self.constants:
                raise NotInAlphabetException()
        self.rules[initiator] = consequence

    def expand(self):
        self.age += 1
        self.state = self._expand(self.state)

    def _expand(self, state):
        next_state = []
        for e in state:
            if isinstance(e, list):
                next_state.append(self._expand(e))
            else:
                if e in self.constants:
                    next_state.append(e)
                    continue
                for initiator, consequence in self.rules.items():
                    if initiator is e:
                        next_state.append(consequence)
        return next_state

    def get_constants(self):
        return list(self.constants)

    def get_variables(self):
        return list(self.variables)

    def get_initiator(self):
        return self.initiator

    def get_age(self):
        return self.age

    def get_state(self):
        return list(self.state)

    def get_rules(self):
        return dict(self.rules)


class TerminalSymbol:

    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s

    def __repr__(self):
        return self.s


class Leaf(TerminalSymbol):

    def __init__(self):
        super().__init__('l')


class Left(TerminalSymbol):

    def __init__(self):
        super().__init__('+')


class Right(TerminalSymbol):
    def __init__(self):
        super().__init__('-')


class Branch:

    def __init__(self, i):
        self.s = 'b' + str(i)

    def __str__(self):
        return self.s

    def __repr__(self):
        return self.s


class NotInAlphabetException(Exception):
    pass


if __name__ == '__main__':
    import random

    tree = Tree()
    [tree.add_branch_type() for i in range(1)]
    initiator = tree.get_initiator()
    constants = tree.get_constants()
    variables = tree.get_variables()

    alphabet = list()
    alphabet.extend(variables)
    alphabet.extend(constants)

    for initiator in variables:
        consequence = []
        for i in range(6):
            consequence.append(random.choice(alphabet))
        tree.add_generating_rule(initiator, consequence)

    age = 5

    for _ in range(age):
        tree.expand()

    [print((k, v)) for k, v in tree.get_rules().items()]
    print(tree.get_state())
