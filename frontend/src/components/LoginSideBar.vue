<template>
	<button v-if="logged" class="btn" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight"
		aria-controls="offcanvasRight">Profile</button>
	<button v-else class="btn" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight"
		aria-controls="offcanvasRight">Login</button>

	<div class="offcanvas offcanvas-end" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
		<div class="offcanvas-header">
			<h5 v-if="tela == 0" class="offcanvas-title" id="offcanvasRightLabel">Login</h5>
			<h5 v-else-if="tela == 1" class="offcanvas-title" id="offcanvasRightLabel">Create Account</h5>
			<button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
		</div>
		<div v-if="tela == 0" class="offcanvas-body">
			<LoginForm />
		</div>
		<div v-else-if="tela == 1" class="offcanvas-body">
			<CreateAccForm />
		</div>
	</div>
</template>

<script>

import LoginForm from "@/components/LoginForm.vue";
import CreateAccForm from "@/components/CreateAccForm.vue";


export default {
	name: 'LoginSideBar',
	data() {
		return {
			tela: 1,
			logged: false,
		}

	},
	components: {
		LoginForm,
		CreateAccForm,
	},

}
</script>

<style scoped lang="scss">
.offcanvas-header {
	background-color: grey;
	width: 100%;
	height: 20%;
	display: flex;
	justify-content: center;
	z-index: -1;

	.offcanvas-title {
		margin-bottom: 0;
		// flex: 1;
	}

}

.offcanvas-body {
	width: 100%;
	top: 20%;
	align-content: center;
	z-index: 999999;
}
</style>