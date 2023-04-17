from dataclasses import dataclass
from typing import List

@dataclass
class LandPlot:
    id: int
    name: str
    description: str
    boundaries: List[float]  # [x1, y1, x2, y2, ...] representing polygon vertices
    beds: List[Bed]  # A list of Bed objects (from the previous Bed data model)
    footpaths: List[Footpath]  # A list of Footpath objects
    buildings: List[Building]  # A list of Building objects

