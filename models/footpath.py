@dataclass
class Footpath:
    id: int
    plot_id: int
    name: str
    boundaries: List[float]  # [x1, y1, x2, y2, ...] representing polygon vertices


