from database import get_connection
from sqlite3 import Error
from typing import List, Tuple

# Adicionar uma nota
def add_note(content: str) -> bool:
    try:
        with get_connection() as conn:
            conn.execute("INSERT INTO notes (content) VALUES (?)", (content,))
        return True
    except Error as e:
        print(f"[Erro ao adicionar nota] {e}")
        return False

# Listar todas as notas
def list_notes() -> List[Tuple]:
    try:
        with get_connection() as conn:
            return conn.execute("SELECT * FROM notes").fetchall()
    except Error as e:
        print(f"[Erro ao listar notas] {e}")
        return []

# Deletar uma nota
def delete_note(note_id: int) -> bool:
    try:
        with get_connection() as conn:
            conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        return True
    except Error as e:
        print(f"[Erro ao deletar nota] {e}")
        return False