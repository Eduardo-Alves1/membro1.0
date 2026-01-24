# Documentação da Integração da API ViaCEP

Este documento explica o que foi feito para integrar a busca de CEP no sistema e como a funcionalidade opera.

## O que foi feito

Para implementar o preenchimento automático de endereço a partir do CEP, foram realizadas as seguintes tarefas:

1.  **Refatoração do Modelo de Dados:**
    *   Foram adicionados os campos `bairro`, `city` (cidade) e `state` (estado) ao modelo `Member` para armazenar o endereço residencial completo do membro, separando-o dos dados de nascimento.

2.  **Criação de uma App de API:**
    *   Uma nova app Django chamada `api` foi criada para isolar a lógica de integrações externas, seguindo as boas práticas de desenvolvimento.

3.  **Desenvolvimento da API Interna:**
    *   Dentro da app `api`, foi criada uma view (`get_address_by_cep`) que serve como uma ponte entre o nosso sistema e a API externa do ViaCEP.
    *   Esta view é mais inteligente, pois ela busca os dados no ViaCEP e os traduz para os IDs correspondentes do nosso banco de dados (encontrando o ID do estado e da cidade).
    *   A busca por estado foi aprimorada para lidar com as diferenças entre a sigla (ex: "SP") retornada pela API e o nome completo (ex: "São Paulo") salvo no banco de dados.

4.  **Aprimoramento do Frontend:**
    *   O script JavaScript nos formulários de cadastro e edição foi melhorado para ser mais robusto e oferecer uma melhor experiência ao usuário.
    *   Agora, o usuário recebe um feedback visual claro durante a busca ("Buscando...") e mensagens de erro explícitas caso o CEP não seja encontrado ou ocorra uma falha.

## Como a Integração Funciona (Fluxo de Dados)

O processo de preenchimento automático ocorre em 7 passos rápidos e transparentes para o usuário:

1.  **Usuário Digita o CEP:** O usuário preenche o campo "CEP" no formulário de cadastro ou edição de membro e move o foco para outro campo.

2.  **JavaScript é Acionado:** O evento de "saída do campo" (blur) aciona o script JavaScript presente na página.

3.  **Chamada para a API Interna:** O script faz uma chamada para a nossa própria API, enviando o CEP digitado. A URL da chamada é, por exemplo: `/api/get-address/01001000/`.

4.  **Backend Recebe a Requisição:** A view `get_address_by_cep` na nossa app `api` recebe o CEP.

5.  **Backend Consulta a API Externa:** O nosso servidor faz uma requisição para a API pública do ViaCEP (ex: `https://viacep.com.br/ws/01001000/json/`).

6.  **Backend Processa os Dados:**
    *   Ao receber a resposta do ViaCEP (contendo logradouro, bairro, localidade, uf, etc.), nosso backend realiza duas buscas em **nosso próprio banco de dados**:
        *   Encontra o objeto `State` correspondente à sigla `uf`.
        *   Encontra o objeto `City` correspondente à `localidade` e ao estado já encontrado.
    *   A view então monta uma resposta JSON contendo os dados do endereço e, mais importante, os **IDs** da cidade e do estado.

7.  **JavaScript Preenche o Formulário:**
    *   O script no frontend recebe a resposta JSON do nosso servidor.
    *   Ele usa os dados recebidos para preencher automaticamente os campos "Endereço", "Bairro", "Estado" e "Cidade" no formulário, usando os IDs para selecionar as opções corretas nos menus de seleção.
    *   Uma mensagem de sucesso ou erro é exibida para o usuário.

Este fluxo garante que a lógica de negócio e a comunicação com APIs externas fiquem no backend, enquanto o frontend apenas exibe os resultados, tornando o sistema mais seguro, organizado e fácil de manter.
