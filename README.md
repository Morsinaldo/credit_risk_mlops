# credit_risk_mlops

## Introduction
Credit risk is something that can generate large profits or large losses depending on the size of the risk. So, to try to mitigate the risk of investors losing money, a machine learning model was created that predicts whether a person will pay back the loan on time or not. Obviously, the model is not 100% accurate, and is even a problem involving ethical issues, since a person could pay the loan strictly on time, even if the algorithm has predicted that he or she would not pay. So the model created is only for didactic and scientific purposes.

The data consists of approved loans from 2007 to 2011 from [Lending Club](www.lendingclub.com), a personal loan company that matches borrowers with people who want to lend money to get a financial return on it. The dataset contains 42537 rows and 52 columns and is available on both the github directory and the [Kaggle](https://www.kaggle.com/datasets/samaxtech/lending-club-20072011-data) website.

## Model Card

<img align="center" src="https://digital.hbs.edu/platform-digit/wp-content/uploads/sites/2/2019/02/LC-Logo-Official-min-1100x200.png" />

So, in general, the notebooks used were divided into 7 parts:

  1. The search for data
  2. Exploratory analysis
  3. Pre-Processing
  4. Tests
  5. Splitting the data between training and testing.
  6. Training
  7. Test

O lending club é um mercado de emprestimos pessoais no qual cada mutuário realiza um cadastro, fornecendo informações como histórico financeiro passado, o motivo do empréstimo e muito mais.

O banco de dados obtido no site  possui um total de 52 colunas e 42537 linhas.

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


## About Us
I (Morsinaldo Medeiros) and Alessandro Neto are students of the Postgraduate Program in Electrical and Computer Engineering (PPgEEC) at the Federal University of Rio Grande do Norte (UFRN). As the first project of the EEC1509 — Machine Learning discipline, we took a classic machine learning model and adapted it to a pipeline, which contains good standardization practices in order to put the created model into production.

## Referências

https://www.kaggle.com/datasets/samaxtech/lending-club-20072011-data  
https://app.dataquest.io

