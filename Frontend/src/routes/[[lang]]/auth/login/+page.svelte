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

<header id="navbar">
    <a href="/{lang}">{langset["back"]}</a>
</header>

<section id="main">
    <div id="img">

    </div>
    <div id="login">
        <form method="POST" action="?/login" autocomplete="off">
            <label for="email">{langset["email_or_username"]}</label>
            <br>
            <input type="text" name="username_or_email" placeholder="User123" required>
            <br>
            <label for="password">{langset["password"]}</label>
            <br>
            <input type="password" name="password" placeholder="password123" required>
            <br>
            <p>{langset["noaccount"]}<a href="/{lang}/auth/register">{langset["registration"]}</a>.</p>
            <br>
            <button type="submit">{langset["login"]}</button>
        </form>
    </div>
</section>

<style>
    p {
        color: var(--on-primary);
    }

    p a {
        text-decoration: underline;
    }

    a {
        color: var(--on-secondary);
        text-decoration: none;
        transition-duration: 0.2s;
    }

    a:hover {
        color: var(--tertiary);
        text-decoration: underline;
    }

    div {
        max-width: 48%;
    }

    label {
        color: var(--on-primary);
    }

    input {
        color: var(--on-secondary);
        background-color: var(--secondary);
        border-color: #2f2f2f;
		border-style: solid;
        border-radius: 3px;
    }

    input:focus {
		outline: none;
	}

    button {
        color: var(--on-secondary);
        background-color: var(--secondary);
        border-style: solid;
        border-color: #2f2f2f;
        border-radius: 3px;
    }
</style>