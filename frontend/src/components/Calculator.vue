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
				<EssGroup />
			</div>
			<div key="Scarabs" v-show="currentScrean === 'Scarabs'" class="carousel-slide scarabs">
				
			</div>
			<div key="Oils" v-show="currentScrean === 'Oils'" class="carousel-slide oils">
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
			</div>
		</div>
	</div>
</template>

<script>
import Slot from './Slot.vue';
import EssGroup from './EssGroup.vue';
export default {
	name: 'tabComponent',
	components: {
		EssGroup,
		Slot
	},
	data() {
		return {
			currentScrean: 'Oils',
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
	position: relative;
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


.carousel-slide[v-show="true"] {
	display: block;
}
</style>