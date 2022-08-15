import re

class Version:
    def __init__(self, version: str):
        self.version = self.set_version(version)
    def __str__(self):
        return f'Версия: {self.version}'
    @staticmethod
    def set_version(version):
        if re.match(r'[0-9].[0-9].[0-9]', version) is None:
            raise ValueError('Формат: X.Y.Z')
        else:
            return version

    def __lt__(self, other):
        return self.version < other.version

    def __le__(self, other):
        return self.version <= other.version

    def __eq__(self, other):
        return self.version == other.version

    def __gt__(self, other):
        return self.version > other.version

    def __ge__(self, other):
        return self.version >= self.other
