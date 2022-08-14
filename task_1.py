from dataclasses import dataclass

@dataclass(order = True, frozen = True)

class Version:
    version: str