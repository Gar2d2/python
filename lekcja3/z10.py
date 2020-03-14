
def zakupy(** lista):
    return sum(int(values) for values in lista.values())


print(zakupy(karaluchy="4", psy="10", adamy=2))
