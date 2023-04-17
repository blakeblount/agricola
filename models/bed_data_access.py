import sqlite3
from typing import List, Optional


def create_bed(bed: Bed) -> int:
    with sqlite3.connect("agricola.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO beds (plot_id, name, crop, boundaries, planting_date, 
                              estimated_harvest_date, watering_schedule, 
                              fertilizing_schedule, crop_spacing, min_yield, 
                              max_yield, other_info)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                bed.plot_id, bed.name, bed.crop, str(bed.boundaries), bed.planting_date,
                bed.estimated_harvest_date, str(bed.watering_schedule),
                str(bed.fertilizing_schedule), bed.crop_spacing, bed.min_yield,
                bed.max_yield, str(bed.other_info)
            )
        )
        conn.commit()
        return cursor.lastrowid


def read_bed(bed_id: int) -> Optional[Bed]:
    with sqlite3.connect("agricola.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM beds WHERE id = ?", (bed_id,))
        result = cursor.fetchone()

        if result:
            return Bed(*result)
        else:
            return None


def read_all_beds() -> List[Bed]:
    with sqlite3.connect("agricola.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM beds")
        result = cursor.fetchall()

        return [Bed(*row) for row in result]


def update_bed(bed: Bed) -> None:
    with sqlite3.connect("agricola.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE beds
            SET plot_id = ?, name = ?, crop = ?, boundaries = ?, planting_date = ?, 
                estimated_harvest_date = ?, watering_schedule = ?, fertilizing_schedule = ?, 
                crop_spacing = ?, min_yield = ?, max_yield = ?, other_info = ?
            WHERE id = ?
            """,
            (
                bed.plot_id, bed.name, bed.crop, str(bed.boundaries), bed.planting_date,
                bed.estimated_harvest_date, str(bed.watering_schedule),
                str(bed.fertilizing_schedule), bed.crop_spacing, bed.min_yield,
                bed.max_yield, str(bed.other_info), bed.id
            )
        )
        conn.commit()


def delete_bed(bed_id: int) -> None:
    with sqlite3.connect("agricola.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM beds WHERE id = ?", (bed_id

