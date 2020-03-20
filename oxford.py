class Oxford:

    def __init__(self, word):

        self.word = word

        self.dictionary = {

            "aback": "to surprise or shock somebody.",
            "abacus": """a frame containing wires with small balls
                        that move along them. It is used as a tool
                        or a toy for counting.""",
            "abandon": """to leave something that you are responsible
                            for, usually permanently.""",
            "abandoned": "left and no longer wanted, used or needed",

        }

        print(self.dictionary[self.word])

