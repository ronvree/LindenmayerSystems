import pygame as pygame
import math

from misc.grammar import Leaf, Left, Right, Tree


class TreeView:

    def __init__(self, tree):
        self.size = self.width, self.height = 6000, 6000
        self.tree = tree
        self.leaf_color = (69, 244, 66)
        self.branch_color = (99, 67, 74)
        self.initiator_position = self.width/2, self.height/2
        self.line_length = 50
        # self.leaf_line_length
        self.line_width = 3
        self.d_angle = 20

    def show(self):
        angle_offset = 3 * 90

        def polar_to_cartesian(theta, r):
           return r * math.cos(math.radians(theta)), r * math.sin(math.radians(theta))

        # def cartesian_to_polar(x, y):
        #     return math.degrees(math.atan(y / x)), math.sqrt(math.pow(x, 2) + math.pow(y, 2))

        def draw(state, pos, angle):
            x, y = pos
            for e in state:
                if isinstance(e, list):
                    dx, dy = polar_to_cartesian(angle + angle_offset, self.line_length)
                    pygame.draw.line(screen, self.branch_color, (x, y), (x + dx, y + dy), self.line_width)
                    x, y = x + dx, y + dy
                    draw(e, (x, y), angle)
                if isinstance(e, Leaf):
                    dx, dy = polar_to_cartesian(angle + angle_offset, self.line_length)
                    pygame.draw.line(screen, self.leaf_color, (x, y), (x + dx, y + dy), self.line_width)
                if isinstance(e, Left):
                    angle += self.d_angle
                if isinstance(e, Right):
                    angle -= self.d_angle

        pygame.init()
        screen = pygame.Surface(self.size)

        state = self.tree.get_state()
        draw(state, self.initiator_position, 0)
        pygame.image.save(screen, 'test.png')


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

    age = 9

    for _ in range(age):
        tree.expand()

    [print((k, v)) for k, v in tree.get_rules().items()]
    print(tree.get_state())

    view = TreeView(tree)
    view.show()





