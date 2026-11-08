class MaintenanceService:
    def __init__(self, conn):
        self.conn = conn

    def log_maintenance(self, equipment_id, action, technician=None, status="scheduled", notes=None):
        self.conn.execute(
            """
            INSERT INTO maintenance_logs (equipment_id, action, technician, status, notes)
            VALUES (?, ?, ?, ?, ?)
            """,
            (equipment_id, action, technician, status, notes),
        )
        self.conn.commit()

    def get_logs_for_equipment(self, equipment_id):
        return self.conn.execute(
            "SELECT * FROM maintenance_logs WHERE equipment_id = ? ORDER BY created_at DESC",
            (equipment_id,),
        ).fetchall()
