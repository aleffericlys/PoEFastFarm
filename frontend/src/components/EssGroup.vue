<template>
	<div class="group">
		<div class="g1">
			<div v-for="i in fst4" :class="'layer l' + i" :key="i">
				<Slot v-for="j in essence_info[i]" :key="j" :conteudo="j" />
			</div>
		</div>
		<div class="g4">
			<div v-for="i in fth4" :class="'layer l' + i" :key="i">
				<Slot v-for="j in essence_info[i]" :key="j" :conteudo="j" />
			</div>
		</div>
	</div>
	<div class="group">
		<div class="g2">
			<div v-for="i in snd4" :class="'layer l' + i" :key="i">
				<Slot v-for="j in essence_info[i]" :key="j" :conteudo="j" />
			</div>
		</div>
		<div class="g5">
			<div v-for="i in fift4" :class="'layer l' + i" :key="i">
				<Slot v-for="j in essence_info[i]" :key="j" :conteudo="j" />
			</div>
		</div>
	</div>
	<div class="group">
		<div class="g3">
			<div v-for="i in trd4" :class="'layer l' + i" :key="i">
				<Slot v-for="j in essence_info[i]" :key="j" :conteudo="j" />
			</div>
		</div>
		<div class="g6">
			<div v-for="i in essence_info['Special']" :class="'layer l' + i" :key="i">
				<Slot :conteudo="i" />
			</div>
		</div>
	</div>
</template>

<script>
import Slot from './Slot.vue';
import { ref, onMounted } from 'vue';
export default {
	name: 'EssGroup',
	components: {
		Slot,
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

<style scoped lang="scss">
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
</style>