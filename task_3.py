class MyCripto:
    alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_cypher = ''

    def __init__(self, cypher=None):
        self.cypher = cypher
        self.let_input()

    def let_input(self):
        inp = int(input('Для шифрования введите - 1, для дешифровки введите - 2 \n'))
        while inp != 'exit':
            # inp = int(input('Для шифрования введите - 1, для дешифровки введите - 2'))
            if self.cypher is None and inp == 1:
                word = input('Введите слово для шифрования \n')
                self.cypher = int(input('Введите ключ для шифрования \n'))
                x = self.encrypt(word)
                print(x)
                break
            elif self.cypher == 2 and self.new_cypher == True:
                self.decrypt()
                break
            else:
                print('Вы не ввели слово для шифрования')

    def encrypt(self, word: str):
        """принимает строку и возвращает зашифрованную строку"""
        try:
            for i in range(len(word)):
                qwe = self.alfavit.find(word.upper()[i])
                self.new_cypher += self.alfavit[qwe + self.cypher]

            return self.new_cypher
        except ValueError:
            print('Использовать только английский алфавит')

    def decrypt(self):
        """расшифровывает переданную строку"""
        decrypt = ''
        for i in range(len(self.new_cypher)):
            qwe = self.alfavit.rfind(self.new_cypher.upper()[i])
            decrypt += self.alfavit[qwe - self.cypher]
        print(decrypt)
