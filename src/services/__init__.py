from flask import Blueprint, jsonify, request

from src.database import get_connection

patient_bp = Blueprint("patients", __name__)


@patient_bp.get("/patients")
def list_patients():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM patients ORDER BY created_at DESC").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])


@patient_bp.post("/patients")
def create_patient():
    payload = request.get_json(silent=True) or {}
    required = ["first_name", "last_name", "room"]
    missing = [field for field in required if not payload.get(field)]
    if missing:
        return jsonify({"error": f"Champs requis manquants : {', '.join(missing)}"}), 400

    conn = get_connection()
    cursor = conn.execute(
        """
        INSERT INTO patients (first_name, last_name, insurance_number, room, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            payload["first_name"],
            payload["last_name"],
            payload.get("insurance_number"),
            payload["room"],
            payload.get("status", "active"),
        ),
    )
    conn.commit()
    patient_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": patient_id, "message": "Patient ajouté"}), 201
