

class Utils:

    @staticmethod
    def ispisiIzbornik(izbornik: dict):
        for opcija in izbornik.keys():
            print(f"{opcija}:\t{izbornik[opcija]}")

        print("_" * 30)

    @staticmethod
    def unesiCijeliBroj(text=None, iterator=None):
        while True:
            try:
                if text is None and iterator is None:
                    return int(input("Unesi broj: "))
                elif text is None and iterator is not None:
                    return int(input(f"Unesi {iterator + 1}. broj: "))
                else:
                    return int(input(text))
            except:
                print("Krivi unos...")

    @staticmethod
    def dodajZnamenke(id, brojZnamenki =3):
        stringID = str(id)
        while len(stringID) < brojZnamenki:
            stringID = "0" + stringID

        return stringID