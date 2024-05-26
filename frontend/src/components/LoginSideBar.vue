<template>
	<button v-if="auth" class="btn" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight"
		aria-controls="offcanvasRight">Profile</button>
	<button v-else class="btn" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight"
		aria-controls="offcanvasRight">Login</button>

	<div class="offcanvas offcanvas-end" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
		<div class="offcanvas-header">
			<h5 v-if="auth" class="offcanvas-title" id="offcanvasRightLabel">Profile</h5>
			<h5 v-else class="offcanvas-title" id="offcanvasRightLabel">Login</h5>
			<button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
		</div>
		<div v-if="auth" class="offcanvas-body">
			<ProfileForm />
		</div>
		<div v-else class="offcanvas-body">
			<LoginForm />
		</div>
	</div>
</template>

<script>
import { computed } from "vue";
import LoginForm from "@/components/LoginForm.vue";
import ProfileForm from "@/components/ProfileForm.vue";
import { useStore } from "vuex";


export default {
	name: 'LoginSideBar',

	components: {
		LoginForm,
		ProfileForm,
	},

	setup() {

		const store = useStore();

		const auth = computed(() => store.state.isAuthenticated);

		return {
			auth,
		}
	}

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