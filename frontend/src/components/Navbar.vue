<template>
	<header>
		<nav class="uk-navbar-container" uk-navbar>
			<div class="uk-navbar-left">
				<ul class="uk-navbar-nav">
					<li class="uk-active uk-text-bold uk-text-center uk-text-large uk-margin-large-left">
						<router-link to="/new">+ Compose</router-link>
					</li>
				</ul>
			</div>
			<div class="uk-navbar-right">
				<ul class="uk-navbar-nav uk-height-match">
					<li class="uk-text-bold uk-text-center uk-text-large uk-margin-left" :class="{ 'uk-active': !isSent }">
						<router-link to="/">inbox</router-link>
					</li>
					<li class="uk-text-bold uk-text-center uk-text-large uk-margin-right" :class="{ 'uk-active': isSent }">
						<router-link to="/sent">sent</router-link>
					</li>
					<li>
						<button @click="logout"
							class="uk-button uk-button-default uk-margin-top uk-margin-large-right uk-margin-left">Logout</button>
					</li>
				</ul>
			</div>
		</nav>
	</header>
</template>

<script>
export default {

	name: 'navbar-header',
	data() {
		return {
			isSent: this.$route.name === "sent-messages"
		}
	},
	methods: {
		logout() {
			localStorage.removeItem('cb_token');
			this.$router.push({ name: 'auth-login' });
		}
	},


}
</script>