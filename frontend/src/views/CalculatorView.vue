<template>
	<div class="about">
		<tabComponent />
	</div>

</template>

<script>
import tabComponent from "@/components/Calculator.vue";
export default {
	components: {
		tabComponent,
	},
};

</script>

<style scoped>
.about {
	display: block;
	position: relative;
	align-items: center;
}
</style>