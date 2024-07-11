<template>
	<div class="oilss">
					<div class="space1">
						<div class="top">
							<div v-for="i in range(7)" class="slotsss">
								<Slot />
							</div>
							
						</div>
						<div class="bott">
							<div v-for="i in range(6)" class="slotsss">
								<Slot />
							</div>
						</div>
					</div>
					<div class="space2">
						<div class="top">
							<div v-for="i in range(2)" class="slotsss">
								<Slot />
							</div>
						</div>
						<div class="bott">
							<div class="slotsss">
								<Slot />
							</div>
						</div>
					</div>
				</div>
</template>

<script>
import Slot from './Slot.vue';
export default {
	name: 'OilGroup',
	components: {
		Slot,
	},
	data() {
		return {
			range(fim) {
				const start = 1; // valor inicial do intervalo
				const end = fim;   // valor final do intervalo
				return Array.from({ length: end - start + 1 }, (_, i) => i + start);
			}
		}
	},
}
</script>

<style scoped>
.oilss {
	width: 92%;
	height: 17%;
	border: red solid 1px;
	position: absolute;
	top: 4%;
	display: flex;
	justify-content: space-between;

	.space1 {
		width: 74%;
		height: 100%;
		border: green solid 1px;
		position: relative;
		left: 2px;
	}

	.space2 {
		width: 20%;
		height: 100%;
		border: blue solid 1px;
		position: relative;
		right: 2px;
	}

	.top, .bott {
		width: 100%;
		height: 50%;
		display: flex;
		
		.slotsss {
			width: 5.55vh;
			height: 100%;
			border: purple solid 1px;
		}
	}
	
	
	.top {
		justify-content: space-between;
		border: yellow solid 1px;
	}
	
	.bott {
		justify-content: center;
		border: pink solid 1px;
		padding-left: 5.8%;
		padding-right: 5.5%;

		.slotsss{
			margin-left: 1.5%;
			margin-right: 1.5%;
		}
	}
}
</style>