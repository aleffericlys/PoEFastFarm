<template>
	<nav>
		<div class="leftSideBar">
			side bar
		</div>
		<div class="links">
			<router-link to="/">
				<div class="home">
					Home
				</div>
			</router-link>
			<router-link to="/calculator">
				<div class="calculator">
					Calculator
				</div>
			</router-link>
		</div>
		<div class="RightSidebar">
			<LoginSideBar />
		</div>
	</nav>
</template>

<script>
import LoginSideBar from "@/components/LoginSideBar.vue";

export default {
	name: "Sidebar",
	components: {
		LoginSideBar,
	},
};

</script>

<style scoped lang="scss">
nav {
	padding-left: 10px;
	padding-right: 10px;
	height: 40px;
	background-color: #d9d9d9;
	display: flex;
	justify-content: space-between;
	align-items: center;


	.links {
		display: flex;
		background-color: #f5f5f5;
		padding: 3px;
		width: 60%;
		height: 80%;
		margin: 0 auto;
		border-radius: 5px;
		align-items: center;
		justify-content: space-around;


		a {
			background-color: #dcdcdc;
			color: #1c1c1c;
			padding: 3px;
			width: 48%;
			height: 90%;
			border-radius: 5px;
			display: flex;
			align-items: center;
			// align-content: center;
			justify-content: center;
			text-decoration: none;

			&.router-link-exact-active {
				color: #ffffff;
				background-color: #444444;
				display: flex;
				align-items: center;
			}

			// .div {
			// 	display: flex;
			// 	background-color: green;
			// 	height: 100%;
			// }
		}
	}
}
</style>