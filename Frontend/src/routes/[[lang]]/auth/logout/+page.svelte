<script>
    // @ts-nocheck
    import translations from "./translations";

    export let data;
    const lang = data.lang
    const langset = translations[lang]
</script>

<svelte:head>
    <title>{langset["title"]}</title>
    <meta name="author" content="DauriaLife" />
</svelte:head>