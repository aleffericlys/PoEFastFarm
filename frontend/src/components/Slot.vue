<template>
	<div :class="[isClicked ? 'click' : 'noClick']" @click="clicked"
		:style="{ 'background-image': isClicked ? 'url(' + url + ')' : 'none' }">
		<div class="popover-container" @mouseover="show = true" @mouseleave="show = false">
			<div v-if="show" class="popover-content">
				
			</div>
		</div>
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
	data() {
		return {
			isClicked: false,
			show: false,
		};
	},
	methods: {
		clicked() {
			this.isClicked = !this.isClicked;
		}
	},
	setup(props) {
		if (props.conteudo) {
			console.log(props.conteudo.name);
			return {
				url: props.conteudo.icon
			}
		} else {
			return {
				url: 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvRXNzZW5jZS9UZXJyb3IxIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/80faa3ee53/Terror1.png'
			}

		}
	}
}
</script>

<style scoped lang="scss">
.popover-container {
  position: relative;
  display: inline-block;
  width: 100%;
  height: 100%;
}

.popover-content {
  display: inline-block;
  position: absolute;
  bottom: 100%; /* Altera de 'top' para 'bottom' para posicionar acima */
  left: 50%;
  transform: translateX(-50%);
  margin-bottom: 10px; /* Espaço entre o elemento e o popover */
  padding: 10px;
  border-radius: 4px;
  background-color: #333;
  color: #fff;
  white-space: nowrap;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  z-index: 10;
}


.click {
	width: 10vh;
	height: 100%;
	background-size: 90% 90%;
	background-repeat: no-repeat;
	background-position: center;
}

.noClick {
	width: 10vh;
	height: 100%;
}
</style>