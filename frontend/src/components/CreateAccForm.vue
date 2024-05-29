<template>
	<form class="login_form" @submit.prevent="submit" enctype="multipart/form-data">
		<div v-if="methods === 'PUT'" class="info">Preencha ou altere apenas os campos que deseja alterar!</div>
		<div v-else class="info">Preencha todos os campos que tem '*' como marcação</div>

		<div class="form-floating">
			<p class="profileInfo">Profile picture:</p>
			<input @change="imageUp" type="file" class="form-control image" id="floatingInput image" name="image" accept="image/*" placeholder="image">
		</div>
		<div class="text-campos">
			<div class="form-floating">
				<input v-if="methods === 'PUT'" v-model="data.email" type="email" class="form-control" id="floatingInput email" placeholder="name@example.com" readonly>
				<input v-else v-model="data.email" type="email" class="form-control" id="floatingInput email" placeholder="name@example.com">
				<label for="floatingInput">Email address*</label>
			</div>

			<div class="form-floating">
				<input v-model="data.name" type="text" class="form-control" id="floatingInput name" placeholder="name">
				<label for="floatingInput">Name*</label>
			</div>

			<div class="form-floating">
				<input v-model="data.nickName" type="text" class="form-control" id="floatingInput nickName"
					placeholder="Nick Name">
				<label for="floatingInput">Nick Name*</label>
			</div>

			<div v-if="methods === 'POST'" class="form-floating">
				<input v-model="data.password" type="password" class="form-control" id="floatingPassword Password"
					placeholder="Password">
				<label for="floatingPassword">Password*</label>
			</div>
		</div>

		<button v-if="methods === 'POST'" class="w-100 btn btn-lg btn-primary" type="submit">Create account</button>
		<button v-else class="w-100 btn btn-lg btn-primary" type="submit">Update account</button>

		<p class="mt-4 mb-3 text-muted">© 2024</p>
	</form>
</template>

<script>
import { reactive, ref } from 'vue';
import { useStore } from 'vuex';

export default {
	name: 'CreateAccForm',

	props: {
		methods: {
			type: String,
			required: true,
		},
	},

	setup(props) {
		const methods = props.methods;
		const user = useStore().state.user;

		const data = reactive({
			email: '',
			name: '',
			nickName: '',
			password: '',
			profilePicture: null,
		});

		if (methods === 'PUT') {
			data.email = user.email;
		}

		const errorMessage = ref(''); // Variável para armazenar a mensagem de erro

		const imageUp = (e) => {
			data.profilePicture = e.target.files[0];
		};

		const submit = async () => {
			try {
				const formData = new FormData(); // Criação do FormData para envio dos dados
				for (const key in data) {
					if (data[key] != '' && data[key] != null) {
						formData.append(key, data[key]);
					}
				}

				const response = await fetch('http://localhost:8000/api/data/', {
					method: methods,
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
				window.location.reload(); // Recarrega a página após o envio bem-sucedido
			} catch (error) {
				console.error('There was a problem with the form submission:', error);
				errorMessage.value = 'There was a problem with the form submission.'; // Exibe mensagem de erro genérica em caso de exceção
			}
		};

		return { data, submit, imageUp, errorMessage };
	},
};

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

.PImage {
	margin-bottom: 10px;
}


.criar_conta {
	position: relative;
	width: 100%;
	display: flex;
	align-items: center;
	justify-content: center;

	.btn {
		margin-left: 5px;
	}
}

.profileInfo {
	margin-right: 70%;
	margin-bottom: -2px;
}

.info {
	color: red;
	font-size: 12px;
}
</style>