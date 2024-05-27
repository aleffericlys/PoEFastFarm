<template>
	<form class="profile_form" @submit="submit">
		<div class="file-container">
			<div class="form-floating image">
				<input @change="imageUp" type="file" class="form-control image" id="floatingInput" name="image"
					accept="image/*" placeholder="image">
			</div>
			<label>profile image</label>
		</div>
		<div class="text-campos">
			<div class="form-floating">
				<input v-model="data.email" type="email" class="form-control" id="floatingInput"
					placeholder="name@example.com">
				<label for="floatingInput">Email address</label>
			</div>

			<div class="form-floating">
				<input v-model="data.name" type="text" class="form-control" id="floatingInput" placeholder="name">
				<label for="floatingInput">Name</label>
			</div>

			<div class="form-floating">
				<input v-model="data.nickName" type="text" class="form-control" id="floatingInput"
					placeholder="Nick Name">
				<label for="floatingInput">Nick Name</label>
			</div>

		</div>

		<button class="w-100 btn btn-lg btn-primary" type="submit">update account</button>
		<div class="criar_conta">
			<button class="btn btn-danger" @click="logout">Realizar Logout!</button>
		</div>
		<p class="mt-4 mb-3 text-muted">© 2024</p>
	</form>
</template>

<script>
import { reactive, ref, computed } from 'vue';
import { useStore } from 'vuex';

export default {
	name: 'ProfileForm',
	setup() {
		const user = useStore().state.user;
		const message = ref('')

		const data = reactive({
			email: user.email,
			name: user.name,
			nickName: user.nickName,
			profilePicture: null,
		})

		const imageUp = (e) => {
			data.profilePicture = e.target.files[0];
		}

		const profilePictureUrl = computed(() => {
			if (user) {
				return "http://localhost:8000/"+user.profilePicture
			}else{
				return "não tem"
			}
			
		});

		const submit = async () => {
			try {
				const formData = new FormData(); // Criação do FormData para envio dos dados
				for (const key in data) {
					formData.append(key, data[key]);
				}

				const response = await fetch('http://localhost:8000/api/data/', {
					method: 'PUT',
					credentials: 'include',
					body: formData, // Enviando o FormData
				});

				if (!response.ok) {
					const errorData = await response.json();
					errorMessage.value = errorData.profilePicture[0] || 'An error occurred'; // Captura e exibe a mensagem de erro do backend
					return;
				}

				const responseData = await response.json();
				console.log('Form submitted successfully:', responseData);
				errorMessage.value = ''; // Limpa as mensagens de erro após um envio bem-sucedido
			} catch (error) {
				console.error('There was a problem with the form submission:', error);
				errorMessage.value = 'There was a problem with the form submission.'; // Exibe mensagem de erro genérica em caso de exceção
			}
		};

		const logout = async () => {
			await fetch('http://localhost:8000/api/logout/', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				credentials: 'include',
			})
			window.location.reload();
		}

		return { data, submit, imageUp, logout, profilePictureUrl }

	}
}

</script>

<style scoped lang="scss">
.profile_form {
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
</style>