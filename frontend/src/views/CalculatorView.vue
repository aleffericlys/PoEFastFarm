<template>
	<div class="about">
		<h1>{{ message }}</h1>
	</div>
</template>

<script>
import { onMounted, ref } from 'vue';
import { useStore } from 'vuex';

export default {
	setup() {
		const store = useStore();
		const message = ref('You are not logged in!');

		onMounted(async () => {
			try {
				const response = await fetch('http://localhost:8000/api/user/', {
					method: 'GET',
					headers: {
						'Content-Type': 'application/json',
					},
					credentials: 'include',
				});
				if (!response.ok) {
					throw new Error('Network response was not ok');
				}
				const data = await response.json();
				if (data.name) {
					store.dispatch('login', data); // Despacha a ação de login
					message.value = `Welcome ${data.name}!`;
				} else {
					console.log(data.message);
				}
			} catch (error) {
				console.error('There has been a problem with your fetch operation:', error);
			}
		});

		return { message };
	},
};
</script>

<style scoped>
.about {
	color: white;
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100%;
}
</style>