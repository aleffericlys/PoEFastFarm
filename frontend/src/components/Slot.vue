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
			required: false,
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
	background-image: url('https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvRXNzZW5jZS9UZXJyb3IxIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/80faa3ee53/Terror1.png');
	// background-size: contain;
	background-repeat: no-repeat;
	background-position: center;
}

.noClick {
	width: 10vh;
	height: 100%;
}
</style>