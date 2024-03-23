# Resultado - Desáfio CoorLab

## Me chamo Matheus Henrique Rodrigues Magalhães, tenho 20 anos e estudo Ciências da Computação pela UFG

# Implementação

### A stack escolhida para o projeto inclui as seguintes tecnologias 

- FastAPI
- Uvicorn
- Vue.js
- Tailwindcss
- Axios

## Back-End
  
### A motivação por trás da escolha do framework FastApi para o backend se deve a sua simplicidade e por ser um framework mais minimalista dado o problema que foi apresentado, haviam outras opções como flask e django porém julguei que utilizando FastApi poderia sintetizar a solução em um único arquivo .py ao invés de utilizar algo com mais boilerplate, além de ser um dos frameworks web mais rápidos em python. O Uvicorn é o web server minimalista que é necessário para rodar nossa API  através da CLI.

### De forma simplificada, temos apenas uma rota no back-end, onde coletamos o nome da cidade por meio de uma requisição HTTP e buscamos os objetos que incluem o nome da cidade em questão através de um laço de iteração, caso não seja encontrada retornamos que a cidade não foi encontrada no arquivo .json . Não utilizei nenhuma forma de Banco de Dados relacional por julgar que o próprio JSON poderia resolver o problema de forma satisfatória.

### Observações: Durante minha implementação encontrei alguns obstáculos, dentre eles, uma das cidades no arquivo data.json continha um erro ortográfico, que foi corrigido reescrevendo no próprio arquivo; o outro erro que encontrei foi referente a forma que o windows codificava acentuações, ao buscar pela cidade "São Paulo" na lista de cidades, no OS Windows 10 não obtinha resultados, mas no Ubuntu sim, para resolver o erro no Windows foi necessário ter uma condicional que ajustasse a string para a forma correta antes de acessar no array de objetos : ```city = city if city != "São Paulo" else "SÃ£o Paulo"```, desta forma, a busca pela requisição da cidade São Paulo ocorreria corretamente quando o servidor da api estivesse rodando no OS Windows, *este código foi removido do repositório na versão final para evitar bugs*.

## Front-End

### Já no front-end as únicas bibliotecas instaladas foram o Axios para as requisições HTTP e o TailwindCSS, visto que tenho maior facilidade e praticidade em fazer estilizações com ele, agilizando o desenvolvimento. No que tange o código desenvolvido o nível de dificuldade foi relativamente simples, separei os inputs do formulário de busca em alguns componentes e passei os respectivos valores como eventos com ```defineEmits``` para o componente pai, e nele foram realizadas as requisições.

### Os componentes do formulário de busca e inputs foram feitos de forma mais nativa possível e sem uso de bibliotecas externas, favorecendo garantia de funcionalidade em detrimento de possibilidade de bugs em algum pacote instalado.

### Observações: Não implementei e passei os valores da Data atual para o back-end por que não entendi exatamente como ela influenciaria na busca de viagens e alteraria a ordem em que seriam exibidas, pois, se a data escolhida no input for apenas uma data qualquer, isso não influenciaria nas viagens selecionadas no array por que apenas temos um valor de duração, valor este que seria o mesmo independente de qual data desejássemos como parâmetro na requisição. Por tanto julguei como desnecessária a inclusão do valor de ```selectedDate``` na requisição para o back-end. 