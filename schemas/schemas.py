import enum


class EpisodeType(str, enum.Enum):
    """Enum to represent the type of episode"""
    MANGA_CANON = 'Manga Canon'
    FILLER = 'Filler'
    MIXED = 'Mixed Canon/Filler'
