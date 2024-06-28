<template>
	<div class="sidebar">
		<div v-for="i in range (20)" class="itens">
			<p>Item {{ i }}</p>
		</div>
	</div>
</template>

<script>
export default {
	name: 'ItensSideBar',
	// Your component's logic goes here
	data() {
		return {
			range(fim) {
				const start = 1; // valor inicial do intervalo
				const end = fim;   // valor final do intervalo
				return Array.from({ length: end - start + 1 }, (_, i) => i + start);
			}
		};
	},
}
</script>

<style scoped>
.sidebar {
	/* Your sidebar styles go here */
	position: fixed;
	top: 40px;
	left: 0;
	width: 10%;
	height: 100vh;
	background-color: grey;
}
.itens {
	/* Your item styles go here */
	display: flex;
	justify-content: center;
	align-items: center;
	width: 100%;
	height: 60px;
	margin: 0px 0px -15px 0px;
	background-color: #555;
}

.itens:hover {
	/* Your item hover styles go here */
	background-color: #333;
}
</style>