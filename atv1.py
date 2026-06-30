# Parte 1 
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

# Parte 2 
l1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
l2 = Livro("O Alquimista", "Paulo Coelho", 1988)
l3 = Livro("Dom Casmurro", "Machado de Assis", 2010) 

# Parte 3 
biblioteca = [l1, l2, l3]

# Parte 4 
def exibir_livro(livro):
    """Imprime os detalhes de um livro individual."""
    print(f"Título: {livro.titulo} | Autor: {livro.autor} | Ano: {livro.ano_publicacao}")

def verificar_duplicados(lista_livros):
    """Verifica duplicidade baseada na combinação de Título e Autor."""
    vistos = set()
    encontrou_duplicado = False
    
    for livro in lista_livros:
        
        chave = (livro.titulo, livro.autor)
        
        if chave in vistos:
            print(f"Duplicado encontrado: {chave}")
            encontrou_duplicado = True
        else:
            vistos.add(chave)
            
    if not encontrou_duplicado:
        print("Nenhum livro duplicado encontrado.")


print("--- Listagem de Livros ---")
for livro in biblioteca:
    exibir_livro(livro)

print("\n--- Verificação de Regra de Negócio ---")
verificar_duplicados(biblioteca)