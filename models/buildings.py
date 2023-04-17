@dataclass
class Building:
    id: int
    plot_id: int
    name: str
    boundaries: List[float]  # [x1, y1, x2, y2, ...] representing polygon vertices
    building_type: str  # e.g., "greenhouse", "barn", "storage"
    other_info: dict  # Additional building-specific information

