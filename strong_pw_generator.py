from random import randrange

class Lists:

    def lists_random(self):
        letters_lower = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        letters_upper = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        especial_characters = [
            ".", ",", ";", "?", "&"
        ]
        numbers = [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        ]
        all_lists = [letters_lower, letters_upper, especial_characters, numbers]
        random_list = all_lists[randrange(start=0, stop=4)]
        return random_list

    def select_list(self):
        list_now = self.lists_random()
        if len(list_now) == 26:
            first_list = list_now[randrange(start=0, stop=26)]
        elif len(list_now) == 5:
            first_list = list_now[randrange(start=0, stop=5)]
        elif len(list_now) == 10:
            first_list = list_now[randrange(start=0, stop=10)]
        return first_list

    def password_convert(self, password):
        password_convert = "".join(map(str, password))
        return password_convert

    def generator_password(self):
        password_in_list = []
        for _ in "passwordsecurity":
            character = str(self.select_list())
            password_in_list.append(character)
        password = self.password_convert(password_in_list)
        return password