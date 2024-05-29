<template>
	<form class="profile_form">
		<div class="file-container">
			<div class="form-floating image">
				<img class="image" :src="profilePictureUrl" alt="">
			</div>
		</div>
		<div class="text-campos">
			<div class="form-floating">
				<input v-model="data.email" type="email" class="form-control" id="floatingInput" placeholder="name@example.com" readonly>
				<label for="floatingInput">Email address</label>
			</div>

			<div class="form-floating">
				<input v-model="data.name" type="text" class="form-control" id="floatingInput" placeholder="name" readonly>
				<label for="floatingInput">Name</label>
			</div>

			<div class="form-floating">
				<input v-model="data.nickName" type="text" class="form-control" id="floatingInput" placeholder="Nick Name" readonly>
				<label for="floatingInput">Nick Name</label>
			</div>

		</div>

		<div class="criar_conta">
			<CreateAccModal methods="PUT"/>
			<button class="btn btn-danger" @click="logout">Realizar Logout!</button>
		</div>
		<p class="mt-4 mb-3 text-muted">© 2024</p>
	</form>
</template>

<script>
import { reactive, computed } from 'vue';
import { useStore } from 'vuex';
import CreateAccModal from './CreateAccModal.vue';

export default {
	name: 'ProfileForm',

	components: {
		CreateAccModal,
	},

	setup() {
		const user = useStore().state.user;

		const data = reactive({
			email: user.email,
			name: user.name,
			nickName: user.nickName,
		});

		const profilePictureUrl = computed(() => {
			if (user) {
				return "http://localhost:8000/" + user.profilePicture
			} else {
				return ""
			}

		});

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

		return { data, logout, profilePictureUrl }

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
	background-color: white;
	width: 150px;
	height: 150px;
	position: relative;
	margin-left: auto;
	margin-right: auto;
	border-radius: 50%;



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
	justify-content: space-evenly;
}
</style>