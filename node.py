from typing import List


class Node:

    def __init__(self, representation, g_score):
        self.representation = representation
        self.h_score = self.generate_heuristic(representation)
        self.g_score = g_score
        self.f_score = self.calculate_evaluation_function()
        self.parent = None

    @staticmethod
    def generate_heuristic(puzzle: List):
        goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        misplaced_tiles = 0
        for index, number in enumerate(puzzle):
            if number != goal_state[index]:
                misplaced_tiles += 1

        return misplaced_tiles

    def calculate_evaluation_function(self):
        # F = H + G
        return self.h_score + self.g_score

    def generate_children(self):
        children = []
        zero_index = self.find_zero()

        if zero_index - 3 >= 0:
            # move zero up
            representation = self.representation.copy()
            representation[zero_index - 3], representation[zero_index] = 0, representation[zero_index - 3]
            temp_node = Node(representation, self.g_score + 1)
            temp_node.parent = self
            children.append(temp_node)

        if zero_index + 3 < len(self.representation):
            # move zero down
            representation = self.representation.copy()
            representation[zero_index + 3], representation[zero_index] = 0, representation[zero_index + 3]
            temp_node = Node(representation, self.g_score + 1)
            temp_node.parent = self
            children.append(temp_node)

        if not zero_index % 3 == 0:
            # move zero left
            representation = self.representation.copy()
            representation[zero_index - 1], representation[zero_index] = 0, representation[zero_index - 1]
            temp_node = Node(representation, self.g_score + 1)
            temp_node.parent = self
            children.append(temp_node)

        if not (zero_index + 1) % 3 == 0:
            # move right
            representation = self.representation.copy()
            representation[zero_index + 1], representation[zero_index] = 0, representation[zero_index + 1]
            temp_node = Node(representation, self.g_score + 1)
            temp_node.parent = self
            children.append(temp_node)

        return children

    def find_zero(self):
        for index, number in enumerate(self.representation):
            if number == 0:
                return index

    def __repr__(self):
        for index, number in enumerate(self.representation):
            print('\t', number, end=" ")
            if (index + 1) % 3 == 0:
                print("\n")

        print('\t-----------')

        return ""

