import tkinter as tk
from tkinter import messagebox

# Classes de Produto e Estoque (mesmo código anterior)

class Produto:
    def __init__(self, nome, codigo, descricao, categoria, preco_compra, preco_venda):
        self.nome = nome
        self.codigo = codigo
        self.descricao = descricao
        self.categoria = categoria
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto, quantidade):
        if produto.codigo in self.produtos:
            self.produtos[produto.codigo]['quantidade'] += quantidade
        else:
            self.produtos[produto.codigo] = {
                'produto': produto,
                'quantidade': quantidade
            }

    def remover_produto(self, codigo_produto, quantidade):
        if codigo_produto in self.produtos:
            if self.produtos[codigo_produto]['quantidade'] >= quantidade:
                self.produtos[codigo_produto]['quantidade'] -= quantidade
                if self.produtos[codigo_produto]['quantidade'] == 0:
                    del self.produtos[codigo_produto]
            else:
                messagebox.showerror("Erro", f"Quantidade insuficiente de {self.produtos[codigo_produto]['produto'].nome} no estoque.")
        else:
            messagebox.showerror("Erro", "Produto não encontrado no estoque.")

    def verificar_produto(self, codigo_produto):
        if codigo_produto in self.produtos:
            return self.produtos[codigo_produto]['produto']
        else:
            return None

    def listar_produtos(self):
        return self.produtos.values()

    def atualizar_preco_venda(self, codigo_produto, novo_preco_venda):
        if codigo_produto in self.produtos:
            self.produtos[codigo_produto]['produto'].preco_venda = novo_preco_venda
        else:
            messagebox.showerror("Erro", "Produto não encontrado no estoque.")

    def gerar_relatorio(self):
        relatorio = "Relatório de Estoque:\n"
        for item in self.produtos.values():
            produto = item['produto']
            quantidade = item['quantidade']
            relatorio += f"Produto: {produto.nome}, Categoria: {produto.categoria}, Quantidade: {quantidade}\n"
        messagebox.showinfo("Relatório de Estoque", relatorio)

    def verificar_produto_acabando(self, codigo_produto, limite_alerta):
        if codigo_produto in self.produtos:
            quantidade = self.produtos[codigo_produto]['quantidade']
            if quantidade <= limite_alerta:
                messagebox.showwarning("Atenção", f"{self.produtos[codigo_produto]['produto'].nome} está com poucas unidades ({quantidade} unidades restantes).")
        else:
            messagebox.showerror("Erro", "Produto não encontrado no estoque.")

# Classe para a interface gráfica
class InterfaceGrafica:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Controle de Estoque")

        # Criando o gerenciador de estoque
        self.estoque = Estoque()

        # Criando os widgets
        self.label_nome = tk.Label(self.master, text="Nome:")
        self.label_codigo = tk.Label(self.master, text="Código:")
        self.label_descricao = tk.Label(self.master, text="Descrição:")
        self.label_categoria = tk.Label(self.master, text="Categoria:")
        self.label_preco_compra = tk.Label(self.master, text="Preço Compra:")
        self.label_preco_venda = tk.Label(self.master, text="Preço Venda:")
        self.label_quantidade = tk.Label(self.master, text="Quantidade:")

        self.entry_nome = tk.Entry(self.master)
        self.entry_codigo = tk.Entry(self.master)
        self.entry_descricao = tk.Entry(self.master)
        self.entry_categoria = tk.Entry(self.master)
        self.entry_preco_compra = tk.Entry(self.master)
        self.entry_preco_venda = tk.Entry(self.master)
        self.entry_quantidade = tk.Entry(self.master)

        self.button_adicionar = tk.Button(self.master, text="Adicionar Produto", command=self.adicionar_produto)
        self.button_remover = tk.Button(self.master, text="Remover Produto", command=self.remover_produto)
        self.button_verificar_acabando = tk.Button(self.master, text="Verificar Produto Acabando", command=self.verificar_acabando)
        self.button_gerar_relatorio = tk.Button(self.master, text="Gerar Relatório", command=self.gerar_relatorio)
        self.button_listar_produtos = tk.Button(self.master, text="Listar Produtos", command=self.listar_produtos)

        # Posicionando os widgets na tela
        self.label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_codigo.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_descricao.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_categoria.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_preco_compra.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_preco_venda.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_quantidade.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=5)
        self.entry_descricao.grid(row=2, column=1, padx=10, pady=5)
        self.entry_categoria.grid(row=3, column=1, padx=10, pady=5)
        self.entry_preco_compra.grid(row=4, column=1, padx=10, pady=5)
        self.entry_preco_venda.grid(row=5, column=1, padx=10, pady=5)
        self.entry_quantidade.grid(row=6, column=1, padx=10, pady=5)

        self.button_adicionar.grid(row=7, column=0, columnspan=2, pady=10)
        self.button_remover.grid(row=8, column=0, columnspan=2, pady=10)
        self.button_verificar_acabando.grid(row=9, column=0, columnspan=2, pady=10)
        self.button_gerar_relatorio.grid(row=10, column=0, columnspan=2, pady=10)
        self.button_listar_produtos.grid(row=11, column=0, columnspan=2, pady=10)

    def adicionar_produto(self):
        nome = self.entry_nome.get()
        codigo = self.entry_codigo.get()
        descricao = self.entry_descricao.get()
        categoria = self.entry_categoria.get()
        preco_compra = float(self.entry_preco_compra.get())
        preco_venda = float(self.entry_preco_venda.get())
        quantidade = int(self.entry_quantidade.get())

        produto = Produto(nome, codigo, descricao, categoria, preco_compra, preco_venda)
        self.estoque.adicionar_produto(produto, quantidade)
        messagebox.showinfo("Sucesso", "Produto adicionado ao estoque.")

    def remover_produto(self):
        codigo = self.entry_codigo.get()
        quantidade = int(self.entry_quantidade.get())
        self.estoque.remover_produto(codigo, quantidade)

    def verificar_acabando(self):
        codigo = self.entry_codigo.get()
        limite_alerta = 3
        self.estoque.verificar_produto_acabando(codigo, limite_alerta)

    def gerar_relatorio(self):
        self.estoque.gerar_relatorio()

    def listar_produtos(self):
        produtos = self.estoque.listar_produtos()
        if produtos:
            relatorio = "Lista de Produtos no Estoque:\n"
            for item in produtos:
                produto = item['produto']
                quantidade = item['quantidade']
                relatorio += f"Produto: {produto.nome}, Categoria: {produto.categoria}, Quantidade: {quantidade}\n"
            messagebox.showinfo("Lista de Produtos", relatorio)
        else:
            messagebox.showinfo("Lista de Produtos", "Não há produtos no estoque.")

def main():
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()

if __name__ == "__main__":
    main()