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
						<div v-for="i in fst4" :class="'layer l' + i" :key="i">
							<Slot v-for="j in essence_info[i]" :key="j" :conteudo=" j "/>
						</div>
					</div>
					<div class="g4">
						<div v-for="i in fth4" :class="'layer l' + i" :key="i">
							<Slot v-for="j in essence_info[i]" :key="j" :conteudo=" j "/>
						</div>
					</div>
				</div>
				<div class="group">
					<div class="g2">
						<div v-for="i in snd4" :class="'layer l' + i" :key="i">
							<Slot v-for="j in essence_info[i]" :key="j" :conteudo=" j "/>
						</div>
					</div>
					<div class="g5">
						<div v-for="i in fift4" :class="'layer l' + i" :key="i">
							<Slot v-for="j in essence_info[i]" :key="j" :conteudo=" j "/>
						</div>
					</div>
				</div>
				<div class="group">
					<div class="g3">
						<div v-for="i in trd4" :class="'layer l' + i" :key="i">
							<Slot v-for="j in essence_info[i]" :key="j" :conteudo=" j "/>
						</div>
					</div>
					<div class="g6">
						<div v-for="i in essence_info['Special']" :class="'layer l' + i" :key="i">
							<Slot :conteudo=" i " />
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
import {ref, onMounted } from 'vue';
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
	},
	setup() {
		const ess = '';
		const essence_info = ref({});
		const fst4 = ['Greed', 'Contempt', 'Hatred', 'Woe']
		const snd4 = ['Fear', 'Anger', 'Torment', 'Sorrow']
		const trd4 = ['Rage', 'Suffering', 'Wrath', 'Doubt']
		const fth4 = ['Loathing', 'Zeal', 'Anguish', 'Spite']
		const fift4 = ['Scorn', 'Envy', 'Misery', 'Dread',]

		onMounted(async () => {
			const response = await fetch('http://127.0.0.1:8000/api/itens/essences/', {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
				},
				credentials: 'include',
			});
			if (!response.ok) {
				console.log('You are not logged in!');
			} else {
				essence_info.value = await response.json();
				
			}

		});

		return {
			ess, essence_info, fst4, snd4, trd4, fth4, fift4
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

		.layer {
			display: flex;
			flex-direction: row-reverse;
		}
	}

	.g2 {
		width: 51%;
		height: 100%;

		.layer {
			display: flex;
			flex-direction: row-reverse;
		}
	}

	.g3 {
		width: 42.5%;
		height: 100%;

		.layer {
			display: flex;
			flex-direction: row-reverse;
		}
	}

	.g4 {
		width: 33.5%;
		height: 100%;
	}

	.g5 {
		width: 25%;
		height: 100%;
	}

	.g6 {
		width: 8%;
		height: 100%;
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