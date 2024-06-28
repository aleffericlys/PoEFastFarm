<template>
	<div class="home">
		<ItensSideBar/>
		<img alt="Vue logo" src="../assets/logo.png">
		<h1>Home Scream</h1>
	</div>
</template>

<script>
// @ is an alias to /src
import ItensSideBar from '@/components/ItensSideBar.vue'

export default {
	name: 'HomeView',
	components: {
		ItensSideBar
	}
}
</script>
<style scoped>
.home {
	color: white;
}
</style>
