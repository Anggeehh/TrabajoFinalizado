#!/usr/bin/env python3
"""Script para crear la base de datos 'reto_angel.db' con la tabla LOGS
e insertar 30 eventos de ejemplo.
"""
import os
import sqlite3
from pathlib import Path


def main():
    # Ruta del script y ubicación de la base de datos en el mismo directorio
    base_dir = Path(__file__).resolve().parent
    db_path = base_dir / 'reto_angel.db'

    # Si existe, eliminar para garantizar una creación limpia
    if db_path.exists():
        try:
            db_path.unlink()
            print(f"Archivo existente eliminado: {db_path}")
        except Exception as e:
            print(f"No se pudo eliminar {db_path}: {e}")

    # Conectar a SQLite y crear tabla
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()

    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS LOGS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evento TEXT NOT NULL
        )
        '''
    )

    # 30 eventos inventados
    eventos = [
        "Inicio sistema",
        "Carga completa",
        "Usuario conectado",
        "Usuario desconectado",
        "Error detectado: E001",
        "Error resuelto: E001",
        "Backup automático",
        "Backup completado",
        "Sincronización iniciada",
        "Sincronización finalizada",
        "Nueva configuración aplicada",
        "Reinicio programado",
        "Servicio A iniciado",
        "Servicio B detenido",
        "Actualización disponible",
        "Actualización instalada",
        "Conexión perdida con servidor",
        "Conexión restablecida",
        "Alerta: uso alto CPU",
        "Alerta: uso alto memoria",
        "Proceso de limpieza ejecutado",
        "Cache vaciada",
        "Permisos actualizados",
        "Acceso no autorizado detectado",
        "Bloqueo de IP temporal",
        "Reporte diario generado",
        "Reporte enviado por correo",
        "Restauración iniciada",
        "Restauración completada",
    ]

    # Insertar eventos
    cur.executemany('INSERT INTO LOGS (evento) VALUES (?)', [(e,) for e in eventos])
    conn.commit()

    # Comprobar conteo
    cur.execute('SELECT COUNT(*) FROM LOGS')
    count = cur.fetchone()[0]

    print(f"Base de datos creada en: {db_path}")
    print(f"Filas insertadas en LOGS: {count}")

    # Mostrar las primeras 5 filas como verificación
    cur.execute('SELECT id, evento FROM LOGS ORDER BY id LIMIT 5')
    rows = cur.fetchall()
    print("Primeras 5 filas:")
    for r in rows:
        print(r)

    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
