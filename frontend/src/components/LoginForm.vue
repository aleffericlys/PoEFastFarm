<template>
	<form class="login_form" @submit="submit">
			<h1 class="h3 mb-3 fw-normal">Entre com Email e Senha</h1>
			
			<div class="form-floating">
				<input v-model="data.email" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
				<label for="floatingInput">Email address</label>
			</div>
			
			<div class="form-floating">
				<input v-model="data.password" type="password" class="form-control" id="floatingPassword" placeholder="Password" value="">
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
import { reactive } from "vue";

export default {
	name: 'LoginForm',
	setup() {
		const data = reactive({
			email: '',
			password: '',
		})

		const submit = async () => {
			await fetch('http://localhost:8000/api/login/', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				credentials: 'include',
				body: JSON.stringify(data),
			})
			window.location.reload();
		}

		return { data, submit }
	}
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