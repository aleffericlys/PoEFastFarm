<template>
	<!-- Button trigger modal -->
	<button type="button" :class=" btnType" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
		{{ btnText }}
	</button>

	<!-- Modal -->
	<div class="modal fade" id="staticBackdrop" data-bs-backdrop="false" data-bs-keyboard="false"
		aria-labelledby="staticBackdropLabel" aria-hidden="true">
		<div class="modal-dialog modal-dialog-scrollable">
			<div class="modal-content">
				<div class="modal-header">
					<h1 class="modal-title fs-5" id="staticBackdropLabel">{{ btnText }}</h1>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					<CreateAccForm :methods="methods"/>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-primary" data-bs-dismiss="modal">Login</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import CreateAccForm from '@/components/CreateAccForm.vue';

export default {
	name: 'CreateAccModal',

	props: {
		methods: {
			type: String,
			required: true,
		},
	},

	computed:{
		btnType(){
			if(this.methods == 'PUT'){
				return ["btn", "btn-lg", "btn-primary"]
			}else{
				return ["btn", "principal"]
			}
		},

		btnText(){
			if(this.methods == 'PUT'){
				return "Update Account"
			}else{
				return "Create Account"
			}
		},
	},

	components: {
		CreateAccForm,
	}
}

</script>

<style scoped lang="scss">
.principal {
	color: #0d6efd;
}
</style>