PRD: Módulo Financeiro - Registro de Dízimos e Ofertas

  1. Visão Geral
  Atualmente, o sistema gerencia o cadastro de membros. A gestão financeira da igreja, especificamente o registro de
  dízimos e ofertas, é frequentemente realizada de forma manual em planilhas ou cadernos, um processo sujeito a erros,
  que consome tempo e dificulta a geração de relatórios.

  Este módulo tem como objetivo integrar ao sistema existente uma ferramenta para o registro digital, seguro e eficiente
  de todas as contribuições financeiras (dízimos e ofertas), centralizando a informação e automatizando parte do
  trabalho do tesoureiro.

  2. Objetivos Principais
   * Centralizar: Criar um registro único e confiável para todas as contribuições.
   * Agilizar: Permitir que o tesoureiro registre novas contribuições de forma rápida.
   * Organizar: Facilitar a consulta e a filtragem dos registros por membro, data ou tipo de contribuição.
   * Informar: Gerar relatórios simples, como a soma das entradas por período, para apoiar a tomada de decisão da
     liderança.

  3. Métricas de Sucesso
   * Adoção: 100% das novas contribuições sendo registradas através do sistema.
   * Eficiência: Redução de pelo menos 50% no tempo gasto pelo tesoureiro para compilar o relatório financeiro mensal.
   * Confiabilidade: Ausência de discrepâncias entre os valores registrados no sistema e os extratos bancários.

  4. Papéis de Usuário (User Roles)
   * Tesoureiro/Administrador:
       * Pode registrar, visualizar, editar e excluir todas as contribuições.
       * Pode gerar relatórios financeiros.
   * Membro/Dizimista (Visão Futura):
       * Poderá visualizar apenas seu próprio histórico de contribuições em um portal pessoal.

  5. Requisitos Funcionais (User Stories)
   * RF-01: Como tesoureiro, eu quero registrar uma nova contribuição, associando-a a um membro, definindo o valor, a
     data, o tipo (dízimo, oferta, etc.) e o método de pagamento, para manter um registro preciso.
   * RF-02: Como tesoureiro, eu quero visualizar uma lista de todas as contribuições registradas, com a capacidade de
     buscar por nome do membro e filtrar por um intervalo de datas, para facilitar auditorias e consultas.
   * RF-03: Como tesoureiro, eu quero editar ou excluir um lançamento, para poder corrigir possíveis erros de digitação.
   * RF-04: Como tesoureiro, eu quero visualizar um painel simples (dashboard) com o valor total arrecadado no mês
     corrente, para ter uma visão rápida da saúde financeira.

  6. Requisitos Técnicos (Plano de Implementação)
  Para atender aos requisitos, planejamos as seguintes alterações no projeto Django:

   * Model: Criar um novo modelo Contribution no arquivo cadmember/models.py com os seguintes campos:
       * member (ForeignKey para Member)
       * value (DecimalField)
       * date (DateField)
       * type (CharField com escolhas: "Dízimo", "Oferta Geral", "Oferta Especial")
       * payment_method (CharField com escolhas: "Dinheiro", "PIX", "Cartão de Débito/Crédito")
       * notes (TextField, opcional)
       * created_at / updated_at (DateTimeField)

   * Views: Desenvolver as seguintes views baseadas em classe:
       * ContributionCreateView para o formulário de registro.
       * ContributionListView para a listagem e filtros.
       * ContributionUpdateView e ContributionDeleteView para edição e exclusão.
       * Uma view para o Dashboard.

   * URLs: Adicionar as rotas para as novas views em cadmember/urls.py.

   * Templates: Criar os arquivos HTML necessários para os formulários e a listagem.

   * Testes: Criar testes unitários para garantir que o modelo e as views funcionam como esperado.

  7. Fora do Escopo (Para esta versão inicial)
   * Portal do membro para visualização do histórico pessoal.
   * Geração de recibos/declarações anuais para imposto de renda.
   * Módulo de controle de despesas (contas a pagar).
   * Ferramentas de orçamento.

8. Novas funcionalidades
   * O sistema deve ter um cadastro de Igrejas. 
     * [ ] Cada igreja deve ter um código único e informações básicas como nome, endereço e contato, CNPJ, Campo Administrativo, Ex (Sudeste, Centro oeste, Nordeste, Norte, Sul).
     * [ ] Deve ser possível associar membros a igrejas específicas.
     * [ ] Deve ser possivel associar "Congregações" que fazem parte do mesmo campo Administrativo. Ex.: (Igreja Cede: A, Congregação: B)
     * [ ] Devemos fazer uma atualização no módulo financeiro, para fazer o balanço mensal das igrejas e das congregações separadamente.
     * [ ] Deve ter filtros específicos.
     * [ ] Cada Igreja Administrativa terá um usuário ADM.
       * [ ] Cada igreja só poderá vizualizar seus próprios dados de sua própria igreja e de susa congregações.