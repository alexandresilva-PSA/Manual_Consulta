Plano de Reconstrução Integral: Manual EFD Contribuições
1. Contexto e Objetivo
O arquivo atual (manual_efd_contribuicoes.html) possui uma estrutura textual válida, mas incompleta visualmente. Temos agora um acervo de 69 imagens (localizadas na pasta imagens total) que narram a jornada do usuário passo a passo.

Objetivo: Reescrever o <body> do manual mantendo a "Engine" (CSS/JS) funcional, mas reestruturando totalmente o conteúdo das seções para acomodar todas as imagens. Não economize em subtítulos e explicações; se há uma imagem, deve haver contexto para ela.

2. Instruções Técnicas para o IDE
Fonte das Imagens: Utilize os arquivos da pasta imagens total.

Caminho no HTML: As tags <img> devem apontar para imagens/[nome-do-arquivo].

Estrutura de Componente: Todas as imagens devem usar o bloco padrão de visualização:

HTML
<div class="img-container">
    <div class="img-wrapper">
        <img src="imagens/NOME_ARQUIVO.png" class="img-screenshot" alt="Descrição Acessível">
    </div>
    <p class="img-caption">Legenda explicativa</p>
</div>
Texto e Tom: Mantenha o tom profissional e técnico. Onde houver novas imagens sem texto correspondente no manual antigo, crie o texto de apoio baseando-se na legenda sugerida no roteiro abaixo.

3. Roteiro de Conteúdo Detalhado (Passo a Passo)
Seção 1: Visão Geral
Manter texto original sobre o que é a ferramenta.

Seção 2: Acesso ao Sistema (Expandido)
Contexto: Detalhar o fluxo desde a homepage até o dashboard.

2.1 Acessando o Portal:

Texto: Acesse o portal PSA Consultores.

Inserir: 01-01-homepage-psa.png (Homepage Padrão).

Inserir: 01-02-homepage-psa-alt.png (Variação da Homepage).

2.2 Seleção de Área (Pré-Login):

Texto: Antes do login, selecione a área de atuação.

Inserir: 01-03-area-equipe-fechado.png (Tela inicial de seleção).

Inserir: 01-04-area-equipe-dropdown.png (Dropdown aberto).

2.3 Autenticação:

Texto: Insira suas credenciais corporativas.

Inserir: 01-05-tela-login.png (Tela vazia).

Inserir: 01-06-login-preenchido.png (Dados preenchidos).

2.4 Seleção de Ambiente:

Texto: Após autenticar, escolha o ambiente "Digital Dev".

Inserir: 01-07-area-digital-escolha.png (Seleção entre Rotina e Dev).

2.5 Acesso à Ferramenta:

Texto: No dashboard, navegue pelo menu lateral.

Inserir: 01-08-dashboard-dev.png (Dashboard Digital Dev).

Seção 3: Filtros de Busca
Contexto: Detalhar o uso dos componentes de data e seleção.

3.1 Visão Inicial:

Inserir: 02-01-filtros-vazio.png (Estado inicial).

3.2 Seleção de Entidade:

Inserir: 02-02-dropdown-cliente.png (Seleção de Cliente).

Inserir: 02-03-dropdown-contribuinte.png (Seleção de Contribuinte).

3.3 Definição de Período:

Texto: Use o calendário para definir datas. Utilize o seletor de ano para navegação rápida.

Inserir: 02-04-calendario-2021.png (Seletor de ano).

Inserir: 02-05-calendario-2026.png (Seleção de mês).

3.4 Execução:

Texto: Com os filtros definidos, realize a busca.

Inserir: 02-06-filtros-preenchidos.png (Estado preenchido 1).

Inserir: 02-07-filtros-preenchidos-alt.png (Estado preenchido variação).

Seção 4: Lista de Arquivos
Contexto: Apresentação dos resultados.

4.1 Grid de Resultados:

Inserir: 03-01-lista-arquivos.png (Lista geral).

Seção 5: Download de Arquivos
Contexto: Fluxo de download individual e em lote.

5.1 Download Individual:

Inserir: 03-02-tooltip-baixar-txt.png (Tooltip no botão).

Inserir: 03-03-toast-download-iniciado.png (Confirmação visual).

5.2 Download em Lote (ZIP):

Inserir: 03-04-tooltip-baixar-todos.png (Botão superior).

Texto: O sistema processará o pacote. Aguarde o indicador de carregamento.

Inserir: 03-05-baixar-todos-loading.png (Estado Loading).

Inserir: 03-06-toast-download-zip.png (Download concluído).

Seção 6: Exportação para Excel (Introdução)
Contexto: Abertura do modal.

6.1 Acesso à Funcionalidade:

Inserir: 04-01-tooltip-exportar-excel.png (Botão na grid).

6.2 Modal de Seleção:

Inserir: 04-02-modal-exportar-inicial.png (Visão geral do modal).

Inserir: 04-03-dropdown-perfil-aberto.png (Dropdown de perfis vazio/inicial).

Seção 7: Seleção de Registros
Contexto: Granularidade da seleção (Blocos e Registros).

7.1 Seleção em Massa:

Inserir: 04-04-todos-registros-selecionados.png (Botão "Selecionar Todos").

7.2 Navegação por Blocos (Bloco 0):

Inserir: 04-05-bloco0-expandido.png (Expandido).

Inserir: 04-06-bloco0-selecao-parcial.png (Seleção parcial).

7.3 Navegação por Blocos (Bloco 1):

Inserir: 04-07-bloco1-expandido.png (Expandido).

Inserir: 04-08-bloco1-selecao-parcial.png (Seleção parcial).

Seção 8: Gestão de Perfis de Exportação (Reestruturação Completa)
Contexto: Criar, usar, alternar e excluir perfis. Esta seção deve ser muito detalhada.

8.1 Criando o Primeiro Perfil:

Texto: Configure sua seleção e clique no botão de adição (+).

Inserir: 04-09-tooltip-salvar-perfil.png (Tooltip no botão +).

Inserir: 05-01-modal-salvar-perfil.png (Modal aberto).

Opção alternativa de modal: 05-02-modal-salvar-perfil-alt.png.

8.2 Configurando o Perfil:

Texto: Defina um nome e escolha se será o padrão.

Inserir: 05-03-nome-perfil-digitado.png (Digitando nome).

Inserir: 05-04-checkbox-perfil-padrao.png (Checkbox marcado).

Variação: 05-05-checkbox-perfil-padrao-alt.png.

Inserir: 05-06-toast-perfil-criado.png (Confirmação).

8.3 Utilizando um Perfil Salvo:

Texto: O perfil aparece na lista com uma estrela (se for favorito).

Inserir: 05-07-perfil-salvo-dropdown.png (Lista com perfil).

Inserir: 05-08-modal-com-perfil.png (Contexto geral).

Inserir: 05-09-modal-perfil-selecionado.png (Perfil carregado).

8.4 Validando o Conteúdo do Perfil:

Texto: Ao carregar, verifique os blocos.

Inserir: 05-10-blocoA-expandido.png (Bloco A expandido).

Inserir: 05-11-blocoA-selecao-parcial.png (Detalhes da seleção).

8.5 Criando Múltiplos Perfis (Variações):

Texto: Crie variações para diferentes análises (Ex: Demonstração 2).

Inserir: 05-12-tooltip-salvar-novo-perfil.png (Novo clique no +).

Inserir: 05-13-modal-salvar-perfil2.png (Novo modal).

Inserir: 05-14-nome-perfil2-digitado.png (Nomeando perfil 2).

Inserir: 05-15-perfil2-como-padrao.png (Definindo novo padrão).

Inserir: 05-16-modal-salvar-perfil2-confirm.png (Salvar).

Inserir: 05-17-toast-perfil2-criado.png (Sucesso).

8.6 Manutenção e Exclusão:

Texto: Gerencie seus perfis. O antigo padrão pode ser excluído se necessário.

Inserir: 05-18-dropdown-multiplos-perfis.png (Lista com vários itens).

Inserir: 05-19-dropdown-icone-excluir.png (Ação de excluir).

Inserir: 05-20-modal-confirmar-exclusao.png (Confirmação).

Inserir: 05-21-toast-perfil-excluido.png (Feedback).

Inserir: 05-22-dropdown-apos-exclusao.png (Lista limpa).

Seção 9: Gerando o Relatório
Contexto: Finalização da exportação.

9.1 Processamento:

Inserir: 06-01-modal-pronto-exportar.png (Botão habilitado).

Inserir: 06-02-exportacao-processando.png (Botão processando).

Inserir: 06-03-toast-exportacao-concluida.png (Conclusão).

Seção 10: Análise de Arquivos (Visualização)
Contexto: Entrada no módulo de análise.

10.1 Iniciando a Análise:

Texto: Identifique o arquivo na lista.

Inserir: 07-01-lista-pre-analise.png (Botão Analisar).

Inserir: 07-02-lista-pre-analise-alt.png (Variação de foco).

10.2 Visão Geral da Análise:

Inserir: 07-03-modal-analise-inicial.png (Modal aberto).

Seção 11: Navegação Estrutural
Contexto: Uso da Sidebar.

11.1 Explorando Blocos:

Inserir: 07-04-sidebar-bloco0-expandido.png (Bloco 0).

Inserir: 07-05-sidebar-blocoC-expandido.png (Bloco C).

Inserir: 07-12-sidebar-todos-blocos.png (Visão completa).

Seção 12: Dados e Interação
Contexto: Manipulação da tabela de dados.

12.1 Carregamento de Dados (Novo):

Texto: Registros volumosos (como C170) podem apresentar estado de carregamento.

Inserir: 07-06-registro-c170-loading.png (Loading Spinner).

12.2 Visualização Tabular:

Inserir: 07-07-tabela-c170-dados.png (Tabela carregada).

12.3 Navegação Horizontal:

Inserir: 07-08-tabela-scroll-horizontal.png (Scroll).

Inserir: 07-09-tabela-scroll-horizontal-alt.png (Variação scroll).

12.4 Interatividade:

Texto: Clique para destacar células ou linhas para facilitar a leitura.

Inserir: 07-10-tabela-celula-selecionada.png (Célula ativa).

Inserir: 07-11-tabela-linha-selecionada.png (Linha ativa).

12.5 Encerrando:

Inserir: 07-13-botao-fechar-modal.png (Botão fechar).

Inserir: 07-14-lista-apos-fechar.png (Retorno à lista).