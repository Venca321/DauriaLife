<script>
    // @ts-nocheck
    import translations from "./translations";

    export let data;
    const lang = data.lang
</script>

<svelte:head>
    <title>{translations[lang]["title"]}</title>
    <meta name="author" content="DauriaLife" />
</svelte:head>

<p>{lang}</p>