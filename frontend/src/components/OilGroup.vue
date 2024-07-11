<template>
	<div class="oilss">
		<div class="space1">
			<div class="top">
				<!-- <div v-for="i in oil_info.top" class="slotsss"> -->
					<Slot v-for="i in oil_info.top" :key="i" :conteudo="i" :oil="true"/>
				<!-- </div> -->

			</div>
			<div class="bott">
				<!-- <div v-for="i in oil_info.bot" class="slotsss"> -->
					<Slot v-for="i in oil_info.bot" :key="i" :conteudo="i" :oil="true"/>
				<!-- </div> -->
			</div>
		</div>
		<div class="space2">
			<div class="top">
					<Slot v-for="i in range(2)" :oil="true"/>
			</div>
			<div class="bott alone">
					<Slot :oil="true"/>
				
			</div>
		</div>
	</div>
</template>

<script>
import Slot from './Slot.vue';
import { ref, onMounted } from 'vue';

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
	setup() {
		const oil_info = ref({});
		onMounted(async () => {
			const response = await fetch('http://127.0.0.1:8000/api/itens/oils/', {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
				},
				credentials: 'include',
			});
			if (!response.ok) {
				console.log('You are not logged in!');
			} else {
				oil_info.value = await response.json();
				console.log(oil_info.value);
			}

		});

		return {
			oil_info
		}
	},
}
</script>

<style scoped>
.oilss {
	width: 92%;
	height: 17%;
	position: absolute;
	top: 4%;
	display: flex;
	justify-content: space-between;

	.space1 {
		width: 74%;
		height: 100%;
		position: relative;
		left: 2px;
	}

	.space2 {
		width: 20%;
		height: 100%;
		position: relative;
		right: 2px;
	}

	.top,
	.bott {
		width: 100%;
		height: 50%;
		display: flex;
	}


	.top {
		justify-content: space-between;
		align-items: center;
		padding-left: 1.5%;
		padding-right: 1.8%;
	}

	.bott {
		justify-content: space-between;
		align-items: center;
		padding-left: 8.6%;
		padding-right: 8.7%;
	}

	.alone {
		justify-content: center;

	}
}
</style>