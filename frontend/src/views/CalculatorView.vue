<template>
	<div class="about">
		<img alt="Vue logo" src="../assets/logo.png">
		<h1>Calculator Scream</h1>
		<tabComponent />
	</div>

</template>

<script>
import tabComponent from "@/components/teste.vue";
export default {
	components: {
		tabComponent,
	},
};

</script>

<style scoped>
.about {
	color: white;
}
</style>