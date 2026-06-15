class ProdutoRepository:
    def __init__(self):
        self._items = []
        self._next_id = 1

    def add(self, data: dict):
        item = {
            "id": self._next_id,
            "codigo": data.get("codigo", "").strip() if data.get("codigo") else "",
            "descricao": data.get("descricao", "").strip() if data.get("descricao") else "",
            "preco": float(data.get("preco", 0.0)) if data.get("preco") not in (None, "") else 0.0,
        }
        self._items.append(item)
        self._next_id += 1
        return item

    def list_all(self):
        return list(self._items)

    def get(self, id: int):
        for it in self._items:
            if it["id"] == id:
                return it
        return None

    def update(self, id: int, data: dict):
        it = self.get(id)
        if not it:
            return None
        if "codigo" in data and data["codigo"] is not None:
            it["codigo"] = data["codigo"].strip()
        if "descricao" in data and data["descricao"] is not None:
            it["descricao"] = data["descricao"].strip()
        if "preco" in data and data["preco"] not in (None, ""):
            it["preco"] = float(data["preco"])
        return it

    def delete(self, id: int):
        it = self.get(id)
        if not it:
            return False
        self._items.remove(it)
        return True
