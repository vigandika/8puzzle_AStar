from operator import attrgetter

from node import Node


class EightPuzzle:

    def solve_8puzzle(self):
        # pseudo-code: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
        open_list = []
        closed_list = []

        start_node = Node([0, 7, 5, 4, 2, 6, 1, 3, 8], 0)
        open_list.append(start_node)

        while len(open_list) > 0:
            # Get node with best (lowest) f_score
            current_node = min(open_list, key=attrgetter('f_score'))
            # if 0 misplaced tiles -> puzzle is solved
            if current_node.h_score == 0:
                self.print_path(current_node)
                break

            open_list.remove(current_node)
            closed_list.append(current_node)

            children = current_node.generate_children()

            for child in children:
                if self.in_list(closed_list, child) != -1:
                    continue

                if (node_index := self.in_list(open_list, child)) != -1:
                    # skip node if there is it exists with a lower g_score
                    if child.g_score >= open_list[node_index].g_score:
                        continue

                open_list.append(child)

    @staticmethod
    def in_list(node_list, current_node):
        """
        Check if node exists in a node list
        :return: index of node in list if it exists, -1 if it does not
        """
        for index, node in enumerate(node_list):
            if node.representation == current_node.representation:
                return index

        return -1

    def print_path(self, current_node):
        if current_node.parent is None:
            print(current_node)
            return

        self.print_path(current_node.parent)
        print(current_node)
        return

    def puzzle_solvable(self):
        """TODO not all 8puzzles are solvable. Check if this one is"""
        # https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable
        pass

if __name__ == '__main__':
    a = EightPuzzle()
    a.solve_8puzzle()
