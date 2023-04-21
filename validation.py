class Validator:
    @staticmethod
    def is_on_board(choice, board):
        return any(choice in row for row in board)

    @staticmethod
    def is_in_range(choice, board_range):
        return choice in board_range

    @staticmethod
    def is_valid_integer(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_there_whitespace(string):
        return len(string.strip()) == len(string)

    @staticmethod
    def is_odd(number):
        return number % 3 == 0

    def validate_size(self, size):
        if not self.is_valid_integer(size):
            return ValidationResult(False, "Eek! That's not even a number! ")

        size = int(size)

        if not self.is_in_range(size, range(3, 6)):
            return ValidationResult(False, "Whoa friend! This is outta bounds! ")

        if not self.is_odd(size):
            return ValidationResult(False, "Ummm. This isn't odd friend!")

        return ValidationResult(True, "")


class ValidationResult:
    def __init__(self, boolean, string):
        self.is_valid = boolean
        self.message = string
