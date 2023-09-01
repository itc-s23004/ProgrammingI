class Nigiri:
    category = "nigiri"
    top = "neta"
    base = "shari"

class katuo(Nigiri):
    top = "katuo"
    topping = "shoga to negi"
    price = 100

    def show_atridubes(self):
        super().show_atridubes()
        print(f"topping: {self.topping}")

k1 = katuo()
k1.show_atridubes()
