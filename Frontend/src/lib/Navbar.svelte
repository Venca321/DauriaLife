
<script lang="ts">
    export let lang:string;
    export let langset:any;
    export let location:string = "";

    let isExpanded = false
	function clickHandler() {
		isExpanded = !isExpanded;
	}
</script>

<header id="navbar">
    <a href="/{lang}"><img src="/images/DauriaLife.png" alt="DariaLife.png"></a>
    <div id="centered">
        <a href="/{lang}#project">{langset["about_project"]}</a>
        <a href="/{lang}#team">{langset["about_us"]}</a>
        <a href="/{lang}#contact">{langset["contact"]}</a>
    </div>
    <button id="lang-button" on:click={clickHandler}>{lang.toUpperCase()}</button>
</header>

{#if isExpanded}
    <section id="dropdown">
        <a target="_self" href="/cz{location}">CZ</a>
        <br>
        <a target="_self" href="/en{location}">EN</a>
    </section>
{/if}

<style>
    #navbar {
        position: fixed;
        z-index: 9999;
        top: 0px;
        left: 0px;
        width: 100%;
        display: inline-flex;
        align-items: center;
        transition: 0.25s;
    }

    #navbar a {
        color: #ffffff;
        text-decoration: none;
        font-size: 18px;
        transition: 0.15s;
    }

    #navbar a:hover {
        color: var(--secondary);
        text-decoration: underline;
    }

    #navbar img {
        height: 32px;
        margin-left: 2vw;
        margin-top: 1.5vh;
        margin-bottom: 0.5vh;
    }

    #dropdown {
        position: fixed;
        text-align: center;
        width: 40px;
        z-index: 999999;
        opacity: 1;
        top: 2vh;
        right: 2.5vw;
        background-color: var(--tertiary);
        border: var(--secondary) 1px solid;
        border-radius: 5px;
    }

    #dropdown a {
        color: var(--on-tertiary);
        text-decoration: none;
        transition: 0.15s;
        padding: 10px 10px 10px 10px;
    }

    #dropdown a:hover {
        color: var(--secondary);
        text-decoration: underline;
    }

    #centered {
        position: absolute;
        left: 50%;
        transform: translate(-50%, 0);
    }

    #centered a {
        margin-right: 4vw;
    }

    #lang-button {
        position: absolute;
        left: 97%;
        transform: translate(-97%, 0);
        color: var(--on-tertiary);
        background-color: #00000000;
        border: none;
        font-family: Arial;
        font-size: 18px;
        transition: 0.15s;
    }

    #lang-button:hover {
        color: var(--secondary);
        text-decoration: underline;
    }
</style>