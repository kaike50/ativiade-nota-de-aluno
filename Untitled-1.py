def verificar_acesso(nome, senha):
    # Verifica se o nome e a senha estão corretos
    nome_valido = nome.lower() == "admin"  # Nome é considerado válido se for "admin" (case insensitive)
    senha_correta = senha == "12345"  # Senha padrão para exemplo
    
    if nome_valido and senha_correta:
        return "Acesso permitido"
    else:
        return "Acesso negado"

# Entrada de dados do usuário
nome = input("Digite o nome de usuário: ").strip()
senha = input("Digite a senha: ").strip()

# Resultado
resultado = verificar_acesso(nome, senha)
print(f"Resultado: {resultado}")
