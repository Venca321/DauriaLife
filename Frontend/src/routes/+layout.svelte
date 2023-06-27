<script lang="ts">
	import '../app.css';
</script>

<slot />

<style>
	:global(:root) {
		--primary: #323232;
		--on-primary: #F5F5F5;
		--secondary: #FFB800;
		--on-secondary: #323232;
		--tertiary: #202020;
		--on-tertiary: #E8E8E8;
	}
</style>