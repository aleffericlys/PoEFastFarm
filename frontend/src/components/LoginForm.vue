<template>
	<form class="login_form">
			<h1 class="h3 mb-3 fw-normal">Entre com Email e Senha</h1>
			
			<div class="form-floating">
				<input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
				<label for="floatingInput">Email address</label>
			</div>
			
			<div class="form-floating">
				<input type="password" class="form-control" id="floatingPassword" placeholder="Password" value="">
				<label for="floatingPassword">Password</label>
			</div>
			
			<button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
			<div class="criar_conta">
				não tem conta?<button class="btn" id="criar_conta">Crie uma conta!</button>
			</div>
			<p class="mt-4 mb-3 text-muted">© 2024</p>
	</form>
</template>

<script>
export default {
	name: 'LoginForm',
}

</script>

<style scoped lang="scss">
.login_form {
	align-content: space-around;
	width: 100%;
	// height: 60%;
	max-width: 90%;
	margin: auto;
	.form-floating {
		margin-bottom: 10px;
	}
}

.criar_conta {
	position: relative;
	width: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
	.btn {
		margin-left: 5px;
		color: blue;
	}
}
</style>