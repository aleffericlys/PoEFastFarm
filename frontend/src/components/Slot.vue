<template>
	<div :class="[isClicked ? 'click' : 'noClick', conteudo && conteudo.canUP ? 'canUP' : '', oil ? 'oil' : '']" @click="clicked"
		:style="{ 'background-image': isClicked ? 'url(' + url + ')' : 'none' }">
		<div class="popover-container" @mouseover="show = true" @mouseleave="show = false">
			<div v-if="show && conteudo" class="popover-content">
				{{ conteudo.name }}<br>
				----------------------------------------------<br>
				chaos value: {{ conteudo.chaosValue }}<br>
				exalted value: {{ conteudo.exaltedValue }}<br>
				divine value: {{ conteudo.divineValue }}<br>
			</div>
		</div>
	</div>


</template>

<script>

export default {
	name: 'Slot',
	props: {
		conteudo: {
			type: Object,
			required: false,
		},
		oil:{
			type: Boolean,
			default: false,
		}
	},
	data() {
		return {
			isClicked: false,
			special: false,
			show: false,
		};
	},
	methods: {
		clicked() {
			this.isClicked = !this.isClicked;
		},
		
	},
	setup(props) {
		if (props.conteudo) {
			return {
				url: props.conteudo.icon
			}
		} else {
			return {
				url: ''
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
	bottom: 100%;
	/* Altera de 'top' para 'bottom' para posicionar acima */
	left: 50%;
	transform: translateX(-50%);
	margin-bottom: 10px;
	/* Espaço entre o elemento e o popover */
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

.tier1 {
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

.canUP {
	border: 1px solid green;
}

.oil{
	height: 80%;
	width: 4.8vh;
}
</style>