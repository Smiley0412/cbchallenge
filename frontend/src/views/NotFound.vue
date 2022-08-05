<template>
	<navbar-header></navbar-header>
  <section class="uk-section" uk-height-viewport="expand: true">
    <div class="uk-container uk-container-small">
      <h1>Page not found</h1>
    </div>
  </section>
	<footer class="uk-section uk-section-default uk-section-small">
		<div class="uk-container">
			<p class="uk-text-small uk-text-center">  Copyright 2022 - ConstructionBevy challenge</p>
		</div>
	</footer>
</template>

<script>
import NavbarHeader from '@/components/Navbar.vue';

export default {
  name: "not-found",
  components: {
		NavbarHeader
	},
}
</script>