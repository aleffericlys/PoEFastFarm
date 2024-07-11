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
				<OilGroup />
			</div>
		</div>
	</div>
</template>

<script>
import OilGroup from './OilGroup.vue';
import EssGroup from './EssGroup.vue';
export default {
	name: 'tabComponent',
	components: {
		EssGroup,
		OilGroup,
	},
	data() {
		return {
			currentScrean: 'Oils',
			slides: [
				{ label: 'Essences' },
				{ label: 'Scarabs' },
				{ label: 'Oils' }
			],
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