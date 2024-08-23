class Medicamento():
    def init (self, nome=None, tipo=None, dosagem=None): 
        self._nome = nome
        self._tipo = tipo 
        self._dosagem = dosagem
        
    def nome(self):
        return self._nome
    
    def tipo(self):
    return "ml" if self._tipo =="liquido" else"un"

dipirona = Medicamento ("Dipirona", "Liquido", "500g")
print (dipirona.nome())
print (dipirona.tipo())
   