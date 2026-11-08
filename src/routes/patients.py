from flask import Blueprint, jsonify, request

from src.database import get_connection

equipment_bp = Blueprint("equipment", __name__)


@equipment_bp.get("/equipment")
def list_equipment():
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM equipment ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])


@equipment_bp.post("/equipment")
def create_equipment():
    payload = request.get_json(silent=True) or {}
    required = ["name", "category", "location"]
    missing = [field for field in required if not payload.get(field)]
    if missing:
        return jsonify({"error": f"Champs requis manquants : {', '.join(missing)}"}), 400

    conn = get_connection()
    cursor = conn.execute(
        """
        INSERT INTO equipment (name, category, location, status, serial_number)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            payload["name"],
            payload["category"],
            payload["location"],
            payload.get("status", "operational"),
            payload.get("serial_number"),
        ),
    )
    conn.commit()
    equipment_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": equipment_id, "message": "Équipement ajouté"}), 201


@equipment_bp.get("/equipment/<int:equipment_id>")
def get_equipment(equipment_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM equipment WHERE id = ?", (equipment_id,)).fetchone()
    conn.close()
    if row is None:
        return jsonify({"error": "Équipement introuvable"}), 404
    return jsonify(dict(row))


@equipment_bp.get("/alerts")
def list_alerts():
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM equipment WHERE status IN ('maintenance_required', 'offline') ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])
