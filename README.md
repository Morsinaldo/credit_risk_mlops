# credit_risk_mlops


## Introdução 
Eu (Morsinaldo Medeiros) e Alessandro Pereira, somos alunos de pós graduação em engenharia da computação pela Universidade Federal do Rio Grande do Norte (UFRN).Como primeiro projeto da matéria EEC1509 - Aprendizagem de Máquina criamos um modelo em machine learning.

## Sobre os dados

<img align="center" src="https://digital.hbs.edu/platform-digit/wp-content/uploads/sites/2/2019/02/LC-Logo-Official-min-1100x200.png" />


O lending club é um mercado de emprestimos pessoais no qual cada mutuário realiza um cadastro, fornecendo informações como histórico financeiro passado, o motivo do empréstimo e muito mais.

O banco de dados obtido no site [Kaggle](https://www.kaggle.com/datasets/samaxtech/lending-club-20072011-data) possui um total de 52 colunas e 42537 linhas.

<details>
<summary>Variáveis utilizadas</summary>
<p align = "left">
<b>loan_amnt</b>  - O valor listado do empréstimo solicitado pelo mutuário.  </br>
<b>int_rate</b> - Taxa de juros do empréstimo.  </br>
<b>installment</b> - O pagamento mensal devido pelo mutuário caso o empréstimo se origine.  </br>
<b>emp_length</b> - Tempo de trabalho em anos.  </br>
<b>annual_inc</b> - Renda anual autodeclarada pelo mutuário durante o registro.  </br>
<b>dti</b> - Índice calculado usando o total de pagamentos mensais da dívida do mutuário sobre o total das obrigações da dívida.  </br>
<b>delinq_2yrs</b> - O número de incidências de inadimplência há mais de 30 dias nos últimos 2 anos.  </br>
<b>inq_last_6mths</b> - O número de consultas nos últimos 6 meses (excluindo consultas de automóveis e hipotecas).  </br>
<b>open_acc</b> - O número de linhas de cédito abertas no arquivo do mutuário.  </br>
<b>pub_rec</b> - Número de registros publicos depreciativos.  </br>
<b>revol_bal</b> - Saldo total rotativo de crédito.  </br>
<b>revol_util</b> - Taxa de utilização da linha rotativa.  </br>
<b>total_acc</b> - Total de linhas de crédito atualmente no arquivo de crédito do mutuário.  </br>
<b>home_ownership</b> - O status de propriedade da casa fornecido pelo mutuário durante o registro. Nossos valores são: ALUGUEL, PRÓPRIO, HIPOTECA, OUTROS.  </br>
<b>verification_status</b> - Indica se a renda foi verificada por LC, não verificada, ou se a fonte de renda foi verificada.  </br>
<b>purpose</b> - Uma categoria fornecida pelo mutuário para a solicitação de empréstimo.  </br>
<b>term</b> - O número de pagamentos do empréstimo. Os valores estão em meses e podem ser 36 ou 60.  </br>
</p> 

</details>

## Objetivos

Nosso trabalho teve início com a análise exploratória dos dados, removendo variáveis redundantes e demais variaveis as quais são seriam apropiadas. Para então criarmos um modelo na qual com as informações selecionadas, conseguir informar os status de impréstimo do mutuário, se ele pagou ou está devendo.


## Referências

https://www.kaggle.com/datasets/samaxtech/lending-club-20072011-data
https://app.dataquest.io

