<template>
		<div :class="[isClicked ? 'click' : 'noClick']" @click="clicked" :style="{ 'background-image': isClicked ? 'url(' + url + ')' : 'none' }">
		</div>
		

</template>

<script>
import { ref } from 'vue';

export default {
	name: 'Slot',
	props: {
		conteudo: {
			type: Object,
			required: false,
		}
	},
	created() {
		const ola = ref();
		if (this.conteudo){

			ola.value= this.conteudo.name;
		}
	},
	data() {
		return {
			isClicked: false,
		};
	},
	methods: {
		clicked() {
			this.isClicked = !this.isClicked;
		}
	},
	setup(props) {
		if (props.conteudo){
			console.log(props.conteudo.name);
			return{
				url: props.conteudo.icon
			}
		}else{
			return{
				url: 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvRXNzZW5jZS9UZXJyb3IxIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/80faa3ee53/Terror1.png'
			}
		
		}
	}
}
</script>

<style scoped lang="scss">
.click {
	width: 10vh;
	height: 100%;
	background-size: 90% 90%;
	// background-image: url('https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvRXNzZW5jZS9EcmVhZDciLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/f867c936c4/Dread7.png');
	background-repeat: no-repeat;
	background-position: center;
}

.noClick {
	width: 10vh;
	height: 100%;
}
</style>