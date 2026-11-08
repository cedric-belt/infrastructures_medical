from dataclasses import dataclass, asdict


@dataclass
class Equipment:
    id: int | None = None
    name: str = ""
    category: str = ""
    location: str = ""
    status: str = "operational"
    serial_number: str | None = None

    def to_dict(self):
        return asdict(self)


@dataclass
class Patient:
    id: int | None = None
    first_name: str = ""
    last_name: str = ""
    insurance_number: str | None = None
    room: str | None = None
    status: str = "active"

    def to_dict(self):
        return asdict(self)
