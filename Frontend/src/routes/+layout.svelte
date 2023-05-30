<script lang="ts">
	import '../app.css';
</script>

<slot />

<style>
	:global(:root) {
		--color-background: #24242f;
		--color-text: #ffffff;
		--color-error: #ff370068;

        --color-gray: #626280;
        --color-primary: #42b17d;
        --color-secondary: #d3e71d;
	}
</style>
