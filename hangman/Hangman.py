class Hangman:
    def __init__(self, word: str, allowed_trys: int):
        self.__word_to_guess = word
        self.__wrong_guessed_letters = []
        self.__correct_guessed_letters = []
        self.__allowed_trys = allowed_trys

    def guess_letter(self, letter: str) -> bool:
        """guess letter of the word_to_guess"""
        if len(letter) != 1:
            raise ValueError(f"Letter '{letter}' is to long")
        if letter.lower() in self.__word_to_guess or letter.upper() in self.__word_to_guess:
            if not letter.lower() in self.__correct_guessed_letters and not letter.upper() in self.__correct_guessed_letters: 
                self.__correct_guessed_letters.append(letter.upper())
            return True
        else:
            if not letter.lower() in self.__wrong_guessed_letters or not letter.upper() in self.__wrong_guessed_letters: 
                self.__wrong_guessed_letters.append(letter.upper())
            return False

    def get_guessed_letters(self) -> bool:
        return tuple(self.__correct_guessed_letters + self.__wrong_guessed_letters)

    def get_number_of_wrong_guessed_letters(self) -> int:
        return len(self.__wrong_guessed_letters)

    def get_uncompleted_word(self) -> tuple:
        word = ()
        for index, letter in enumerate(self.__word_to_guess):
            if letter.upper() in self.__correct_guessed_letters or letter.lower() in self.__correct_guessed_letters:
                word = tuple(word + (self.__word_to_guess[index],))
            else:
                word = tuple(word + ("",))
        return word

    def is_finished(self) -> bool:
        return self.__allowed_trys <= self.get_number_of_wrong_guessed_letters()

    def is_won(self) -> bool:
        return self.__word_to_guess == self.get_uncompleted_word()

    def get_word(self) -> str:
        if self.is_finished() or self.is_won():
            return self.__word_to_guess