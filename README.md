<img src="https://user-images.githubusercontent.com/101838119/203919902-4f25739a-29ff-4dee-adf1-b2b681246873.png">
<h1>⚙️ Super OrgContact API </h1>

<p> Este repositório foi desenvolvido em Flask para realizar as requisições do Frontend da aplicação Super OrgContact. </P>

<hr>

<h2> ✔️ ENDPOINT: (POST) /users/auth/google </h2>

<p> Esse endpoint ao realizar a requisição retorna a URL para realizar o seu login com a conta Google no APP. </p>

<hr>

<h2>  ✔️ ENDPOINT: (GET) /users/callback </h2>

<p> Esse endpoint é o callback do Google onde pega as informações do usuario e o retorna ao Frontend </p>

<hr>

<h2> ✔️ ENDPOINT: (POST) /contacts/get </h2> 

<h5> Body params: <h5>


```js
{
    "token": "exemeplodetoken" 
}
```

<p> Pega informações de Nome e Email dos contatos atrelados à conta Google do usuario e as retorna para o frontend. </p>

<hr>

<h1>📝 Considerações</h1>

<p> Nenhum dado particular é armazenado nessa aplicação, todo e qualquer armazenamento é feito no localStorage do frontend do próprio usuário. </p>
