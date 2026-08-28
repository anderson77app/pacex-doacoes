import streamlit as st

# Inicializa o "banco de dados" na memória da sessão do usuário
if 'estoque' not in st.session_state:
    st.session_state.estoque = {}

# Configuração visual do título da página
st.title("📦 Sistema Solidário de Doações")
st.write("Bem-vindo ao portal de controle de estoque da ONG.")

st.divider() # Cria uma linha separadora visual

# SESSÃO 1: CADASTRO DE DOAÇÕES
st.header("➕ Cadastrar Nova Doação")

# Organiza a tela em duas colunas para os campos de digitação
col1, col2 = st.columns(2)
with col1:
    novo_item = st.text_input("Nome do Item:", placeholder="Ex: Arroz, Leite")
with col2:
    nova_qtd = st.number_input("Quantidade:", min_value=1, step=1)

# Ação do botão de adicionar
if st.button("Adicionar ao Estoque"):
    if novo_item:
        item_padronizado = novo_item.strip().upper()
        if item_padronizado in st.session_state.estoque:
            st.session_state.estoque[item_padronizado] += nova_qtd
        else:
            st.session_state.estoque[item_padronizado] = nova_qtd
        st.success(f"Sucesso! {nova_qtd} de '{item_padronizado}' cadastrado.")
    else:
        st.warning("Por favor, digite o nome do item.")

st.divider()

# SESSÃO 2: VISUALIZAÇÃO DO ESTOQUE
st.header("📋 Estoque Atual")
if not st.session_state.estoque:
    st.info("O estoque está vazio no momento.")
else:
    # Transforma o dicionário em um formato visual de tabela
    dados_tabela = {"Item": list(st.session_state.estoque.keys()), 
                    "Quantidade": list(st.session_state.estoque.values())}
    st.table(dados_tabela)

st.divider()

# SESSÃO 3: SAÍDA/ENTREGA DE DOAÇÕES
st.header("➖ Retirar Doação (Entrega)")
if st.session_state.estoque:
    # Cria um menu dropdown (caixa de seleção) com os itens que existem no estoque
    item_retirar = st.selectbox("Selecione o item para retirar:", list(st.session_state.estoque.keys()))
    qtd_retirar = st.number_input("Quantidade a retirar:", min_value=1, step=1, key="retirar")
    
    if st.button("Confirmar Retirada"):
        if qtd_retirar <= st.session_state.estoque[item_retirar]:
            st.session_state.estoque[item_retirar] -= qtd_retirar
            st.success(f"Retirada confirmada! Restam {st.session_state.estoque[item_retirar]}.")
            
            # Remove o item da lista se o estoque dele chegar a zero
            if st.session_state.estoque[item_retirar] == 0:
                del st.session_state.estoque[item_retirar]
                st.rerun() # Atualiza a tela para remover o item visualmente
        else:
            st.error("Erro: Quantidade solicitada é maior que o estoque disponível!")
else:
    st.write("Não há itens no estoque para retirar.")
