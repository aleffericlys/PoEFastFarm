<template>
	<form class="login_form">
		<div class="file-container">
			<div class="form-floating image">
				<input type="file" class="form-control image" id="floatingInput" name="image" accept="image/*"
					placeholder="image">
			</div>
			<label>profile image</label>
		</div>
		<div class="text-campos">
			<div class="form-floating">
				<input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
				<label for="floatingInput">Email address</label>
			</div>

			<div class="form-floating">
				<input type="text" class="form-control" id="floatingInput" placeholder="name">
				<label for="floatingInput">Name</label>
			</div>

			<div class="form-floating">
				<input type="text" class="form-control" id="floatingInput" placeholder="Nick Name">
				<label for="floatingInput">Nick Name</label>
			</div>

			<div class="form-floating">
				<input type="password" class="form-control" id="floatingPassword" placeholder="Password">
				<label for="floatingPassword">Password</label>
			</div>
		</div>

		<button class="w-100 btn btn-lg btn-primary" type="submit">Create account</button>
		<div class="criar_conta">
			já tem conta?<button class="btn" id="criar_conta">Realizar Login!</button>
		</div>
		<p class="mt-4 mb-3 text-muted">© 2024</p>
	</form>
</template>

<script>
export default {
	name: 'CreateAccForm',
}

</script>

<style scoped lang="scss">
.login_form {
	align-content: space-around;
	width: 100%;
	// height: 60%;
	max-width: 90%;
	margin: auto;
	z-index: 999999;

	.form-floating {
		margin-bottom: 10px;

	}
}

.file-container {
	position: absolute;
	top: 11%;
	left: 0;
	width: 100%;
	z-index: 999;
	/* Certifique-se de que a div sobreponha o cabeçalho do offcanvas */
}

.text-campos {
	margin-top: 20%;
}

.image {
	// position: absolute;
	display: flex;
	align-content: center;
	

	.image {
		// position: absolute;
		display: fixed;
		width: 150px;
		height: 150px;
		position: relative;
		margin-left: auto;
		margin-right: auto;
		border-radius: 50%;
		border: 3px solid white;
	}

	label {
		position: absolute;
		margin-left: auto;
		margin-right: auto;
		transform: translate(-50%, -50%);
		color: black;
		font-size: 20px;
		font-weight: bold;
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