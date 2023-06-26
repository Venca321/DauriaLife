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
        <form method="POST" action="?/register" autocomplete="off">
            <label for="name">{langset["name"]}</label>
            <br>
            <input type="text" name="name" placeholder="Honza Novák" required>
            <br>
            <label for="username">{langset["username"]}</label>
            <br>
            <input type="text" name="username" placeholder="User123" required>
            <br>
            <label for="email">{langset["email"]}</label>
            <br>
            <input type="email" name="email" placeholder="name@fake.mail" required>
            <br>
            <label for="password">{langset["password"]}</label>
            <br>
            <input type="password" name="password" placeholder="password123" required>
            <br>
            <label for="password2">{langset["password2"]}</label>
            <br>
            <input type="password" name="password2" placeholder="password123" required>
            <br>
            <p>{langset["haveaccount"]}<a href="/{lang}/auth/login">{langset["login"]}</a>.</p>
            <br>
            <button type="submit">{langset["register"]}</button>
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