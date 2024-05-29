<template>
	<div class="carousel-container">
		<div class="carousel-buttons">
			<button v-for="slide in slides" :key="slide.label" @click="goToSlide(slide.label)"
				:class="[isActiveSlide(slide.label) ? 'btn-active' : 'btn-conf']">
				{{ slide.label }}
			</button>
		</div>
		<div class="carousel-content">
			<div key="Essences" v-show="currentScrean === 'Essences'" class="carousel-slide essences">
				<div class="group">
					<div class="g1">
						<div v-for="i in range(4)" :class="'layer l' + i">
							<!-- <div v-for="j in range(7)" class="slot">{{ j }}</div> -->
							<Slot v-for="j in range(7)" />
						</div>
					</div>
					<div class="g4">
						<div v-for="i in range(4)" :class="'layer l' + i">
							<!-- <div v-for="j in range(4)" class="slot">{{ j }}</div> -->
							<Slot v-for="j in range(4)"/>
						</div>
					</div>
				</div>
				<div class="group">
					<div class="g2">
						<div v-for="i in range(4)" :class="'layer l' + i">
							<!-- <div v-for="j in range(6)" class="slot"></div> -->
							<Slot v-for="j in range(6)"/>
						</div>
					</div>
					<div class="g5">
						<div v-for="i in range(4)" :class="'layer l' + i">
							<!-- <div v-for="j in range(3)" class="slot">{{ j }}</di -->
							<Slot v-for="j in range(3)"/>
						</div>
					</div>
				</div>
				<div class="group">
					<div class="g3">
						<div v-for="i in range(4)" :class="'layer l' + i">
							<!-- <div v-for="j in range(5)" class="slot"></div> -->
							<Slot v-for="j in range(5)"/>
						</div>
					</div>
					<div class="g6">
						<div v-for="i in range(4)" :class="'layer l' + i">
							<!-- <div v-for="j in range(2)" class="slot">{{ j }}</div> -->
							<Slot v-for="j in range(2)"/>
						</div>
					</div>
				</div>

			</div>
			<div key="Scarabs" v-show="currentScrean === 'Scarabs'" class="carousel-slide scarabs">

			</div>
			<div key="Oils" v-show="currentScrean === 'Oils'" class="carousel-slide oils">

			</div>
		</div>
	</div>
</template>

<script>
import Slot from './Slot.vue';
export default {
	name: 'tabComponent',
	components: {
		Slot,
	},
	data() {
		return {
			currentScrean: 'Essences',
			slides: [
				{ label: 'Essences' },
				{ label: 'Scarabs' },
				{ label: 'Oils' }
			],
			range(fim) {
				const start = 1; // valor inicial do intervalo
				const end = fim;   // valor final do intervalo
				return Array.from({ length: end - start + 1 }, (_, i) => i + start);
			}
		};
	},
	methods: {
		goToSlide(Screan) {
			this.currentScrean = Screan;
		},
		isActiveSlide(screan) {
			return this.currentScrean === screan;
		}
	}
}
</script>

<style scoped>
.carousel-container {
	display: flex;
	width: 100%;
	height: 94vh;
	flex-direction: column;
	align-items: center;
	justify-content: center;
}

.carousel-buttons {
	width: 50vh;
	margin-bottom: 5px;
}

.carousel-buttons button {
	width: 30%;
	margin: 5px;
	border-radius: 7px;
}

.carousel-buttons .btn-conf {
	background-color: #f5f5f5;
	color: black;
	/* Adicione outros estilos desejados para o botão não ativo */
}

.carousel-buttons .btn-active {
  background-color: #444444;
  color: white;
  /* Adicione outros estilos desejados para o botão ativo */
}


.carousel-content {
	width: 70vh;
	height: 70vh;
	display: flex;
	justify-content: center;
	align-items: center;
}

.carousel-slide {
	color: white;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
}

.essences {
	width: 100%;
	height: 100%;
	background-image: url('https://web.poecdn.com/protected/image/inventory/EssenceStashPanelGrid.png?v=1713677508135&key=lv_AedXr4s5nRGYe3HSuEQ');
	background-size: contain;
	background-repeat: no-repeat;
}

.oils {
	width: 100%;
	height: 100%;
	background-image: url('https://web.poecdn.com/protected/image/inventory/BlightTabBackground.png?v=1713677508135&key=7iGAVZ6boVdCTi0xPGiY9A');
	background-size: contain;
	background-repeat: no-repeat;
}

.scarabs {
	width: 100%;
	height: 100%;
	background-image: url('https://web.poecdn.com/protected/image/layout/stash/fragment-tab/background-scarab.png?v=1713843145436&key=ybXsvy3pX-mvgPTsg2OBCg');
	background-size: contain;
	background-repeat: no-repeat;
}

.group {
	width: 92%;
	height: 31%;
	display: flex;
	justify-content: space-between;

	.g1 {
		width: 59.5%;
		height: 100%;
	}

	.g2 {
		width: 51%;
		height: 100%;

		.slot {
			width: 10vh;
			height: 100%;
			border: 1px solid blue;
		}
	}

	.g3 {
		width: 42.5%;
		height: 100%;

		.slot {
			width: 10vh;
			height: 100%;
			border: 1px solid blue;
		}
	}

	.g4 {
		width: 33.5%;
		height: 100%;

		.layer {
			display: flex;
			flex-direction: row-reverse;
		}

		.slot {
			width: 10vh;
			height: 100%;
			border: 1px solid blue;
		}
	}

	.g5 {
		width: 25%;
		height: 100%;

		.layer {
			display: flex;
			flex-direction: row-reverse;
		}

		.slot {
			width: 10vh;
			height: 100%;
			border: 1px solid blue;
		}
	}

	.g6 {
		width: 16.5%;
		height: 100%;

		.layer {
			display: flex;
			flex-direction: row-reverse;
		}

		.slot {
			width: 10vh;
			height: 100%;
			border: 1px solid blue;
		}
	}

	.layer {
		width: 100%;
		height: 25%;
		display: flex;
	}
}


.carousel-slide[v-show="true"] {
	display: block;
}
</style>