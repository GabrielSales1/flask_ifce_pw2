class AdminDAO:
    def __init__(self):
        self._admins = []
        self._next_id = 1

    def add(self, data: dict):
        admin = {
            "id": self._next_id,
            "nome": data.get("nome", "").strip() if data.get("nome") else "",
            "senha": data.get("senha", "")
        }
        self._admins.append(admin)
        self._next_id += 1
        return admin

    def list_all(self):
        return list(self._admins)

    def get(self, id: int):
        for a in self._admins:
            if a["id"] == id:
                return a
        return None

    def update(self, id: int, data: dict):
        a = self.get(id)
        if not a:
            return None
        if "nome" in data and data["nome"] is not None:
            a["nome"] = data["nome"].strip()
        if "senha" in data and data["senha"] is not None:
            a["senha"] = data["senha"]
        return a

    def delete(self, id: int):
        a = self.get(id)
        if not a:
            return False
        self._admins.remove(a)
        return True
