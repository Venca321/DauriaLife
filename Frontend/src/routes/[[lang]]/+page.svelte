<script>
    // @ts-nocheck
    import translations from "./translations";

    export let data;
    const lang = data.lang
    const langset = translations[lang]
</script>

<svelte:head>
    <title>DauriaLife</title>
    <meta name="author" content="DauriaLife" />
</svelte:head>

<header id="navbar">
    <div>
        <a id="logo" href="/{lang}">--Logo--</a>
        <a href="/{lang}#about">{langset["about"]}</a>
        <a href="/{lang}#product">{langset["product"]}</a>
        <a href="/{lang}#pro">{langset["pro"]}</a>
        <a href="/{lang}/auth/login">{langset["start"]}</a>
        <a id="lang_button">CZ</a>
    </div>
</header>

<p>{lang}</p>

<style>
    #navbar {
        position: fixed;
        height: 6vh;
        width: 100%;
        top: 0;
        left: 0;
        background-color: var(--secondary);
        text-align: center;
    }

    #navbar div {
        margin-top: 1.3vh;
    }

    #navbar div a {
        color: var(--on-secondary);
        text-decoration: none;
        margin-right: 3%;
        transition-duration: 0.2s;
        text-decoration: none;
    }

    #navbar div a:hover {
        color: var(--tertiary);
        text-decoration: underline;
    }

    #logo{
        padding-right: 30vw;
    }

    #lang_button{
        margin-left: 30vw;
    }
</style>