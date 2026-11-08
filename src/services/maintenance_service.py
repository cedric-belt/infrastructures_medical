class EquipmentService:
    def __init__(self, conn):
        self.conn = conn

    def get_operational_equipment(self):
        return self.conn.execute(
            "SELECT * FROM equipment WHERE status = 'operational' ORDER BY name"
        ).fetchall()

    def get_critical_equipment(self):
        return self.conn.execute(
            "SELECT * FROM equipment WHERE status IN ('maintenance_required', 'offline') ORDER BY name"
        ).fetchall()
