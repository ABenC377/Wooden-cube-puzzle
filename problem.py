class Puzzle:

    def __init__(self):
        self.state = self.make_new_puzzle()
        self.failing_assignments = set()
        self.pieces_placed = []

    def make_new_row(self):
        new_row = []
        for i in range(5):
            new_row.append(chr(9725))
        return new_row

    def make_new_layer(self):
        new_layer = []
        for i in range(5):
            new_layer.append(self.make_new_row())
        return new_layer

    def make_new_puzzle(self):
        new_puzzle = []
        for i in range(5):
            new_puzzle.append(self.make_new_layer())
        return new_puzzle

    def possible_piece_positions(self, assignment, starting_unit):
        # this method takes an index of a single unit, and returns
        # all the possible ways that said unit could be occupied by a new piece
        available_positions = []
        layer = starting_unit[0]
        column = starting_unit[1]
        row = starting_unit[2]
        # using the following numbering of the pieces:
        #  1  2
        #     3  4  5

        # we will start by trying unit 1 at index a
        possible_positions = [[[layer, column, row], [layer + 1, column, row], [layer + 1, column + 1, row], [layer + 2, column + 1, row], [layer + 3, column + 1, row]],
                            [[layer, column, row], [layer + 1, column, row], [layer + 1, column - 1, row], [layer + 2, column - 1, row], [layer + 3, column - 1, row]],
                            [[layer, column, row], [layer + 1, column, row], [layer + 1, column, row + 1], [layer + 2, column, row + 1], [layer + 3, column, row + 1]],
                            [[layer, column, row], [layer + 1, column, row], [layer + 1, column, row - 1], [layer + 2, column, row - 1], [layer + 3, column, row - 1]],
                            [[layer, column, row], [layer - 1, column, row], [layer - 1, column + 1, row], [layer - 2, column + 1, row], [layer - 3, column + 1, row]],
                            [[layer, column, row], [layer - 1, column, row], [layer - 1, column - 1, row], [layer - 2, column - 1, row], [layer - 3, column - 1, row]],
                            [[layer, column, row], [layer - 1, column, row], [layer - 1, column, row + 1], [layer - 2, column, row + 1], [layer - 3, column, row + 1]],
                            [[layer, column, row], [layer - 1, column, row], [layer - 1, column, row - 1], [layer - 2, column, row - 1], [layer - 3, column, row - 1]],
                            [[layer, column, row], [layer, column + 1, row], [layer + 1, column + 1, row], [layer + 1, column + 2, row], [layer + 1, column + 3, row]],
                            [[layer, column, row], [layer, column + 1, row], [layer - 1, column + 1, row], [layer - 1, column + 2, row], [layer - 1, column + 3, row]],
                            [[layer, column, row], [layer, column + 1, row], [layer, column + 1, row + 1], [layer, column + 2, row + 1], [layer, column + 3, row + 1]],
                            [[layer, column, row], [layer, column + 1, row], [layer, column + 1, row - 1], [layer, column + 2, row - 1], [layer, column + 3, row - 1]],
                            [[layer, column, row], [layer, column - 1, row], [layer + 1, column - 1, row], [layer + 1, column - 2, row], [layer + 1, column - 3, row]],
                            [[layer, column, row], [layer, column - 1, row], [layer - 1, column - 1, row], [layer - 1, column - 2, row], [layer - 1, column - 3, row]],
                            [[layer, column, row], [layer, column - 1, row], [layer, column - 1, row + 1], [layer, column - 2, row + 1], [layer, column - 3, row + 1]],
                            [[layer, column, row], [layer, column - 1, row], [layer, column - 1, row - 1], [layer, column - 2, row - 1], [layer, column - 3, row - 1]],
                            [[layer, column, row], [layer, column, row + 1], [layer + 1, column, row + 1], [layer + 1, column, row + 2], [layer + 1, column, row + 3]],
                            [[layer, column, row], [layer, column, row + 1], [layer - 1, column, row + 1], [layer - 1, column, row + 2], [layer - 1, column, row + 3]],
                            [[layer, column, row], [layer, column, row + 1], [layer, column + 1, row + 1], [layer, column + 1, row + 2], [layer, column + 1, row + 3]],
                            [[layer, column, row], [layer, column, row + 1], [layer, column - 1, row + 1], [layer, column - 1, row + 2], [layer, column - 1, row + 3]],
                            [[layer, column, row], [layer, column, row - 1], [layer + 1, column, row - 1], [layer + 1, column, row - 2], [layer + 1, column, row - 3]],
                            [[layer, column, row], [layer, column, row - 1], [layer - 1, column, row - 1], [layer - 1, column, row - 2], [layer - 1, column, row - 3]],
                            [[layer, column, row], [layer, column, row - 1], [layer, column + 1, row - 1], [layer, column + 1, row - 2], [layer, column + 1, row - 3]],
                            [[layer, column, row], [layer, column, row - 1], [layer, column - 1, row - 1], [layer, column - 1, row - 2], [layer, column - 1, row - 3]],
                            # now add the positions with unit 2 at index a
                            [[layer + 1, column, row], [layer, column, row], [layer, column + 1, row], [layer - 1, column + 1, row], [layer - 2, column + 1, row]],
                            [[layer + 1, column, row], [layer, column, row], [layer, column - 1, row], [layer - 1, column - 1, row], [layer - 2, column - 1, row]],
                            [[layer + 1, column, row], [layer, column, row], [layer, column, row + 1], [layer - 1, column, row + 1], [layer - 2, column, row + 1]],
                            [[layer + 1, column, row], [layer, column, row], [layer, column, row - 1], [layer - 1, column, row - 1], [layer - 2, column, row - 1]],
                            [[layer - 1, column, row], [layer, column, row], [layer, column + 1, row], [layer + 1, column + 1, row], [layer + 2, column + 1, row]],
                            [[layer - 1, column, row], [layer, column, row], [layer, column - 1, row], [layer + 1, column - 1, row], [layer + 2, column - 1, row]],
                            [[layer - 1, column, row], [layer, column, row], [layer, column, row + 1], [layer + 1, column, row + 1], [layer + 2, column, row + 1]],
                            [[layer - 1, column, row], [layer, column, row], [layer, column, row - 1], [layer + 1, column, row - 1], [layer + 2, column, row - 1]],
                            [[layer, column + 1, row], [layer, column, row], [layer + 1, column, row], [layer + 1, column - 1, row], [layer + 1, column - 2, row]],
                            [[layer, column + 1, row], [layer, column, row], [layer - 1, column, row], [layer - 1, column - 1, row], [layer - 1, column - 2, row]],
                            [[layer, column + 1, row], [layer, column, row], [layer, column, row + 1], [layer, column - 1, row + 1], [layer, column - 2, row + 1]],
                            [[layer, column + 1, row], [layer, column, row], [layer, column, row - 1], [layer, column - 1, row - 1], [layer, column - 2, row - 1]],
                            [[layer, column - 1, row], [layer, column, row], [layer + 1, column, row], [layer + 1, column + 1, row], [layer + 1, column + 2, row]],
                            [[layer, column - 1, row], [layer, column, row], [layer - 1, column, row], [layer - 1, column + 1, row], [layer - 1, column + 2, row]],
                            [[layer, column - 1, row], [layer, column, row], [layer, column, row + 1], [layer, column + 1, row + 1], [layer, column + 2, row + 1]],
                            [[layer, column - 1, row], [layer, column, row], [layer, column, row - 1], [layer, column + 1, row - 1], [layer, column + 2, row - 1]],
                            [[layer, column, row + 1], [layer, column, row], [layer + 1, column, row], [layer + 1, column, row - 1], [layer + 1, column, row - 2]],
                            [[layer, column, row + 1], [layer, column, row], [layer - 1, column, row], [layer - 1, column, row - 1], [layer - 1, column, row - 2]],
                            [[layer, column, row + 1], [layer, column, row], [layer, column + 1, row], [layer, column + 1, row - 1], [layer, column + 1, row - 2]],
                            [[layer, column, row + 1], [layer, column, row], [layer, column - 1, row], [layer, column - 1, row - 1], [layer, column - 1, row - 2]],
                            [[layer, column, row - 1], [layer, column, row], [layer + 1, column, row], [layer + 1, column, row + 1], [layer + 1, column, row + 2]],
                            [[layer, column, row - 1], [layer, column, row], [layer - 1, column, row], [layer - 1, column, row + 1], [layer - 1, column, row + 2]],
                            [[layer, column, row - 1], [layer, column, row], [layer, column + 1, row], [layer, column + 1, row + 1], [layer, column + 1, row + 2]],
                            [[layer, column, row - 1], [layer, column, row], [layer, column - 1, row], [layer, column - 1, row + 1], [layer, column - 1, row + 2]],
                            # now add the positions with unit 3 at index a
                            [[layer + 1, column + 1, row], [layer, column + 1, row], [layer, column, row], [layer - 1, column, row], [layer - 2, column, row]],
                            [[layer + 1, column - 1, row], [layer, column - 1, row], [layer, column, row], [layer - 1, column, row], [layer - 2, column, row]],
                            [[layer + 1, column, row + 1], [layer, column, row + 1], [layer, column, row], [layer - 1, column, row], [layer - 2, column, row]],
                            [[layer + 1, column, row - 1], [layer, column, row - 1], [layer, column, row], [layer - 1, column, row], [layer - 2, column, row]],
                            [[layer - 1, column + 1, row], [layer, column + 1, row], [layer, column, row], [layer + 1, column, row], [layer + 2, column, row]],
                            [[layer - 1, column - 1, row], [layer, column - 1, row], [layer, column, row], [layer + 1, column, row], [layer + 2, column, row]],
                            [[layer - 1, column, row + 1], [layer, column, row + 1], [layer, column, row], [layer + 1, column, row], [layer + 2, column, row]],
                            [[layer - 1, column, row - 1], [layer, column, row - 1], [layer, column, row], [layer + 1, column, row], [layer + 2, column, row]],
                            [[layer + 1, column + 1, row], [layer + 1, column, row], [layer, column, row], [layer, column - 1, row], [layer, column - 2, row]],
                            [[layer - 1, column + 1, row], [layer - 1, column, row], [layer, column, row], [layer, column - 1, row], [layer, column - 2, row]],
                            [[layer, column + 1, row + 1], [layer, column, row + 1], [layer, column, row], [layer, column - 1, row], [layer, column - 2, row]],
                            [[layer, column + 1, row - 1], [layer, column, row - 1], [layer, column, row], [layer, column - 1, row], [layer, column - 2, row]],
                            [[layer + 1, column - 1, row], [layer + 1, column, row], [layer, column, row], [layer, column + 1, row], [layer, column + 2, row]],
                            [[layer - 1, column - 1, row], [layer - 1, column, row], [layer, column, row], [layer, column + 1, row], [layer, column + 2, row]],
                            [[layer, column - 1, row + 1], [layer, column, row + 1], [layer, column, row], [layer, column + 1, row], [layer, column + 2, row]],
                            [[layer, column - 1, row - 1], [layer, column, row - 1], [layer, column, row], [layer, column + 1, row], [layer, column + 2, row]],
                            [[layer + 1, column, row + 1], [layer + 1, column, row], [layer, column, row], [layer, column, row - 1], [layer, column, row - 2]],
                            [[layer - 1, column, row + 1], [layer - 1, column, row], [layer, column, row], [layer, column, row - 1], [layer, column, row - 2]],
                            [[layer, column + 1, row + 1], [layer, column + 1, row], [layer, column, row], [layer, column, row - 1], [layer, column, row - 2]],
                            [[layer, column - 1, row + 1], [layer, column - 1, row], [layer, column, row], [layer, column, row - 1], [layer, column, row - 2]],
                            [[layer + 1, column, row - 1], [layer + 1, column, row], [layer, column, row], [layer, column, row + 1], [layer, column, row + 2]],
                            [[layer - 1, column, row - 1], [layer - 1, column, row], [layer, column, row], [layer, column, row + 1], [layer, column, row + 2]],
                            [[layer, column + 1, row - 1], [layer, column + 1, row], [layer, column, row], [layer, column, row + 1], [layer, column, row + 2]],
                            [[layer, column - 1, row - 1], [layer, column - 1, row], [layer, column, row], [layer, column, row + 1], [layer, column, row + 2]],
                            # now add the positions with unit 4 at index a
                            [[layer + 2, column + 1, row], [layer + 1, column + 1, row], [layer + 1, column, row], [layer, column, row], [layer - 1, column, row]],
                            [[layer + 2, column - 1, row], [layer + 1, column - 1, row], [layer + 1, column, row], [layer, column, row], [layer - 1, column, row]],
                            [[layer + 2, column, row + 1], [layer + 1, column, row + 1], [layer + 1, column, row], [layer, column, row], [layer - 1, column, row]],
                            [[layer + 2, column, row - 1], [layer + 1, column, row - 1], [layer + 1, column, row], [layer, column, row], [layer - 1, column, row]],
                            [[layer - 2, column + 1, row], [layer - 1, column + 1, row], [layer - 1, column, row], [layer, column, row], [layer + 1, column, row]],
                            [[layer - 2, column - 1, row], [layer - 1, column - 1, row], [layer - 1, column, row], [layer, column, row], [layer + 1, column, row]],
                            [[layer - 2, column, row + 1], [layer - 1, column, row + 1], [layer - 1, column, row], [layer, column, row], [layer + 1, column, row]],
                            [[layer - 2, column, row - 1], [layer - 1, column, row - 1], [layer - 1, column, row], [layer, column, row], [layer + 1, column, row]],
                            [[layer + 1, column + 2, row], [layer + 1, column + 1, row], [layer, column + 1, row], [layer, column, row], [layer, column - 1, row]],
                            [[layer - 1, column + 2, row], [layer - 1, column + 1, row], [layer, column + 1, row], [layer, column, row], [layer, column - 1, row]],
                            [[layer, column + 2, row + 1], [layer, column + 1, row + 1], [layer, column + 1, row], [layer, column, row], [layer, column - 1, row]],
                            [[layer, column + 2, row - 1], [layer, column + 1, row - 1], [layer, column + 1, row], [layer, column, row], [layer, column - 1, row]],
                            [[layer + 1, column - 2, row], [layer + 1, column - 1, row], [layer, column - 1, row], [layer, column, row], [layer, column + 1, row]],
                            [[layer - 1, column - 2, row], [layer - 1, column - 1, row], [layer, column - 1, row], [layer, column, row], [layer, column + 1, row]],
                            [[layer, column - 2, row + 1], [layer, column - 1, row + 1], [layer, column - 1, row], [layer, column, row], [layer, column + 1, row]],
                            [[layer, column - 2, row - 1], [layer, column - 1, row - 1], [layer, column - 1, row], [layer, column, row], [layer, column + 1, row]],
                            [[layer + 1, column, row + 2], [layer + 1, column, row + 1], [layer, column, row + 1], [layer, column, row], [layer, column, row - 1]],
                            [[layer - 1, column, row + 2], [layer - 1, column, row + 1], [layer, column, row + 1], [layer, column, row], [layer, column, row - 1]],
                            [[layer, column + 1, row + 2], [layer, column + 1, row + 1], [layer, column, row + 1], [layer, column, row], [layer, column, row - 1]],
                            [[layer, column - 1, row + 2], [layer, column - 1, row + 1], [layer, column, row + 1], [layer, column, row], [layer, column, row - 1]],
                            [[layer + 1, column, row - 2], [layer + 1, column, row - 1], [layer, column, row - 1], [layer, column, row], [layer, column, row + 1]],
                            [[layer - 1, column, row - 2], [layer - 1, column, row - 1], [layer, column, row - 1], [layer, column, row], [layer, column, row + 1]],
                            [[layer, column + 1, row - 2], [layer, column + 1, row - 1], [layer, column, row - 1], [layer, column, row], [layer, column, row + 1]],
                            [[layer, column - 1, row - 2], [layer, column - 1, row - 1], [layer, column, row - 1], [layer, column, row], [layer, column, row + 1]],
                            # finally, add the positions with unit 5 at position a
                            [[layer + 3, column + 1, row], [layer + 2, column + 1, row], [layer + 2, column, row], [layer + 1, column, row], [layer, column, row]],
                            [[layer + 3, column - 1, row], [layer + 2, column - 1, row], [layer + 2, column, row], [layer + 1, column, row], [layer, column, row]],
                            [[layer + 3, column, row + 1], [layer + 2, column, row + 1], [layer + 2, column, row], [layer + 1, column, row], [layer, column, row]],
                            [[layer + 3, column, row - 1], [layer + 2, column, row - 1], [layer + 2, column, row], [layer + 1, column, row], [layer, column, row]],
                            [[layer - 3, column + 1, row], [layer - 2, column + 1, row], [layer - 2, column, row], [layer - 1, column, row], [layer, column, row]],
                            [[layer - 3, column - 1, row], [layer - 2, column - 1, row], [layer - 2, column, row], [layer - 1, column, row], [layer, column, row]],
                            [[layer - 3, column, row + 1], [layer - 2, column, row + 1], [layer - 2, column, row], [layer - 1, column, row], [layer, column, row]],
                            [[layer - 3, column, row - 1], [layer - 2, column, row - 1], [layer - 2, column, row], [layer - 1, column, row], [layer, column, row]],
                            [[layer + 1, column + 3, row], [layer + 1, column + 2, row], [layer, column + 2, row], [layer, column + 1, row], [layer, column, row]],
                            [[layer - 1, column + 3, row], [layer - 1, column + 2, row], [layer, column + 2, row], [layer, column + 1, row], [layer, column, row]],
                            [[layer, column + 3, row + 1], [layer, column + 2, row + 1], [layer, column + 2, row], [layer, column + 1, row], [layer, column, row]],
                            [[layer, column + 3, row - 1], [layer, column + 2, row - 1], [layer, column + 2, row], [layer, column + 1, row], [layer, column, row]],
                            [[layer + 1, column - 3, row], [layer + 1, column - 2, row], [layer, column - 2, row], [layer, column - 1, row], [layer, column, row]],
                            [[layer - 1, column - 3, row], [layer - 1, column - 2, row], [layer, column - 2, row], [layer, column - 1, row], [layer, column, row]],
                            [[layer, column - 3, row + 1], [layer, column - 2, row + 1], [layer, column - 2, row], [layer, column - 1, row], [layer, column, row]],
                            [[layer, column - 3, row - 1], [layer, column - 2, row - 1], [layer, column - 2, row], [layer, column - 1, row], [layer, column, row]],
                            [[layer + 1, column, row + 3], [layer + 1, column, row + 2], [layer, column, row + 2], [layer, column, row + 1], [layer, column, row]],
                            [[layer - 1, column, row + 3], [layer - 1, column, row + 2], [layer, column, row + 2], [layer, column, row + 1], [layer, column, row]],
                            [[layer, column + 1, row + 3], [layer, column + 1, row + 2], [layer, column, row + 2], [layer, column, row + 1], [layer, column, row]],
                            [[layer, column - 1, row + 3], [layer, column - 1, row + 2], [layer, column, row + 2], [layer, column, row + 1], [layer, column, row]],
                            [[layer + 1, column, row - 3], [layer + 1, column, row - 2], [layer, column, row - 2], [layer, column, row - 1], [layer, column, row]],
                            [[layer - 1, column, row - 3], [layer - 1, column, row - 2], [layer, column, row - 2], [layer, column, row - 1], [layer, column, row]],
                            [[layer, column + 1, row - 3], [layer, column + 1, row - 2], [layer, column, row - 2], [layer, column, row - 1], [layer, column, row]],
                            [[layer, column - 1, row - 3], [layer, column - 1, row - 2], [layer, column, row - 2], [layer, column, row - 1], [layer, column, row]],
                            ]

        available_positions = []

        for position in possible_positions:
            is_available = True
            for unit in position:
                layer, column, row = unit
                if (layer < 0) or (layer > 4) or (column < 0) or (column > 4) or (row < 0) or (row > 4) or (assignment[layer][column][row] == chr(9726)):
                    is_available = False
            if is_available:
                available_positions.append(position)
        return available_positions

    def select_best_empty_unit(self, assignment):
        best_unit = None
        lowest_number_of_possible_piece_positions = None
        for i in range(len(assignment)):
            for j in range(len(assignment[i])):
                for k in range(len(assignment[i][j])):
                    if assignment[i][j][k] == chr(9725):
                        unit = [i, j, k]
                        number_of_possible_piece_positions = len(self.possible_piece_positions(assignment, unit))
                        if lowest_number_of_possible_piece_positions == None or number_of_possible_piece_positions < lowest_number_of_possible_piece_positions:
                            best_unit = unit
                            lowest_number_of_possible_piece_positions = number_of_possible_piece_positions
        return best_unit

    def play_piece(self, position, assignment):
        was_piece_played = False
        for unit in position:
            layer, column, row = unit
            if assignment[layer][column][row] == chr(9726):
                return (was_piece_played, assignment)
        was_piece_played = True
        for unit in position:
            layer, column, row = unit
            assignment[layer][column][row] = chr(9726)
        return (was_piece_played, assignment)

    def remove_piece(self, position, assignment):
        for unit in position:
            layer, column, row = unit
            assignment[layer][column][row] = chr(9725)
        return assignment

    def assignment_to_string(self, assignment):
        output_string = ''
        for layer in assignment:
            for column in assignment:
                for unit in column:
                    output_string += str(unit)
        return output_string

    def backtrack(self, assignment):
        unfilled_unit = self.select_best_empty_unit(assignment)
        if unfilled_unit == None:
            return assignment
        available_piece_positions = self.possible_piece_positions(assignment, unfilled_unit)
        for position in available_piece_positions:
            was_piece_played, assignment = self.play_piece(position, assignment)
            if was_piece_played == False:
                continue
            if self.assignment_to_string(assignment) in self.failing_assignments:
                assignment = self.remove_piece(position, assignment)
            else:
                self.print_assignment(assignment)
                self.pieces_placed.append(position)
                result = self.backtrack(assignment)
                if result != None and self.select_best_empty_unit(result) == None:
                    return result
                self.failing_assignments.add(self.assignment_to_string(assignment))
                assignment = self.remove_piece(position, assignment)
                self.pieces_placed.pop()
        return None

    def print_assignment(self, assignment):
        layer1 = assignment[0]
        layer2 = assignment[1]
        layer3 = assignment[2]
        layer4 = assignment[3]
        layer5 = assignment[4]

        row11 = ' '.join(layer1[0])
        row12 = ' '.join(layer1[1])
        row13 = ' '.join(layer1[2])
        row14 = ' '.join(layer1[3])
        row15 = ' '.join(layer1[4])
        row21 = ' '.join(layer2[0])
        row22 = ' '.join(layer2[1])
        row23 = ' '.join(layer2[2])
        row24 = ' '.join(layer2[3])
        row25 = ' '.join(layer2[4])
        row31 = ' '.join(layer3[0])
        row32 = ' '.join(layer3[1])
        row33 = ' '.join(layer3[2])
        row34 = ' '.join(layer3[3])
        row35 = ' '.join(layer3[4])
        row41 = ' '.join(layer4[0])
        row42 = ' '.join(layer4[1])
        row43 = ' '.join(layer4[2])
        row44 = ' '.join(layer4[3])
        row45 = ' '.join(layer4[4])
        row51 = ' '.join(layer5[0])
        row52 = ' '.join(layer5[1])
        row53 = ' '.join(layer5[2])
        row54 = ' '.join(layer5[3])
        row55 = ' '.join(layer5[4])

        string = '\n\n{c11}   {c21}   {c31}   {c41}   {c51}\n{c12}   {c22}   {c32}   {c42}   {c52}\n{c13}   {c23}   {c33}   {c43}   {c53}\n{c14}   {c24}   {c34}   {c44}   {c54}\n{c15}   {c25}   {c35}   {c45}   {c55}'.format(c11=row11, c12=row12, c13=row13, c14=row14, c15=row15, c21=row21, c22=row22, c23=row23, c24=row24, c25=row25, c31=row31, c32=row32, c33=row33, c34=row34, c35=row35, c41=row41, c42=row42, c43=row43, c44=row44, c45=row45, c51=row51, c52=row52, c53=row53, c54=row54, c55=row55)
        print(string)

    def position_to_string(self, position):
        output_string = ''
        for i in range(len(position)):
            layer, column, row = position[i]
            unit_string = 'Layer {layer}, Column {column}, Row {row}\n'.format(layer = layer, column = column, row = row)
            output_string += unit_string
        return output_string



puzzle = Puzzle()
starting_assignment = puzzle.state
solution = puzzle.backtrack(starting_assignment)
if solution is None:
    print("No solution.")
else:
    print("Solved.")
    for i in range(len(puzzle.pieces_placed)):
        piece_string = 'Piece number {i} placed at:\n'.format(i = i + 1) + puzzle.position_to_string(puzzle.pieces_placed[i]) + '\n\n'
        print(piece_string)
