from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class WateringSchedule:
    frequency: int  # in days
    duration: int  # in minutes
    start_time: str  # in format "HH:MM"

@dataclass
class FertilizingSchedule:
    frequency: int  # in days
    fertilizer_type: str
    amount: float  # in weight units (e.g., grams, ounces)

@dataclass
class Bed:
    id: int
    plot_id: int
    name: str
    crop: str
    boundaries: List[float]  # [x1, y1, x2, y2, ...] representing polygon vertices
    planting_date: datetime
    estimated_harvest_date: datetime
    watering_schedule: WateringSchedule
    fertilizing_schedule: FertilizingSchedule
    crop_spacing: float  # in distance units (e.g., centimeters, inches)
    min_yield: float  # in weight units (e.g., kilograms, pounds)
    max_yield: float  # in weight units (e.g., kilograms, pounds)
    other_info: dict  # Additional crop-specific information

