<template>
	<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
  Create Account
</button>

<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="false" data-bs-keyboard="false" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">Create Account</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <CreateAccForm />
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

	components: {
		CreateAccForm,
	}
}

</script>

<style scoped lang="scss"></style>