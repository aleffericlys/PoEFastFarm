<template>
	<div class="about">
		<h1>{{ mensage }}</h1>
	</div>
</template>

<script>
import { onMounted, ref } from 'vue';
export default {
	setup() {
		const mensage = ref('You are not logged in!');

		onMounted(async () => {
			const response = await fetch('http://localhost:8000/api/user/', {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
				},
				credentials: 'include',
			});
			const data = await response.json();
			if (data.message) {
				console.log(data.message);
			} else {
				mensage.value = `Welcome ${data.name}!`;
			}
		});
		return { mensage };
	}
}
</script>


<style scoped>
.about {
	color: white;
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100vh;
}
</style>