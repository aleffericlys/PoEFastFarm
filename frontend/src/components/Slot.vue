<template>
	<div :class="[isClicked ? 'click' : 'noClick']" @click="clicked">
		{{ conteudo }}
	</div>
</template>

<script>

export default {
	name: 'Slot',
	props: {
		conteudo: {
			type: String,
			required: false
		}
	},
	data() {
		return {
			isClicked: false
		};
	},
	methods: {
		clicked() {
			this.isClicked = !this.isClicked;
		}
	}
}

</script>

<style scoped lang="scss">

.click {
	width: 10vh;
	height: 100%;
	border: 1px solid blue;
}

.noClick {
	width: 10vh;
	height: 100%;
}
</style>