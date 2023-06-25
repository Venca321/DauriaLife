<script lang="ts">
	import '../app.css';
</script>

<slot />

<style>
	:global(:root) {
		--primary: #444444;
		--on-primary: #F5F5F5;
		--secondary: #323232;
		--on-secondary: #E8E8E8;
		--tertiary: #FFB800;
		--on-tertiary: #363636;
	}
</style>
