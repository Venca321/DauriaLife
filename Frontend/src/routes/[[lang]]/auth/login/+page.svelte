<script>
    // @ts-nocheck
    import Navbar from "$lib/Navbar.svelte";
    import translations from "./translations";

    export let data;
    const lang = data.lang
    const langset = translations[lang]
</script>

<svelte:head>
    <title>{langset["title"]}</title>
    <meta name="author" content="DauriaLife" />
</svelte:head>

<Navbar lang={lang} langset={langset} location="/auth/login"/>

<div id="picture">
    <img src="/images/calendar.png" alt="calendar.png">
</div>

<span id="picture-box"></span>
<span id="login-box"></span>

<div id="login">
    <h1>{langset["title"]}</h1>
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
        <div>
            <a id="back-button" href="/{lang}">{langset["back"]}</a>
            <button type="submit">{langset["login"]}</button>
        </div>
    </form>
</div>

<style>
    #picture {
        position: absolute;
        top: 40vh;
        left: 10vw;
        opacity: 0.8;
    }

    #picture img {
        width: 50vw;
        max-height: 58vh;
    }
    
    #picture-box {
        position: absolute;
        top: 0px;
        left: 0px;
        height: 100%;
        width: 50%;
        background: radial-gradient(95.47% 62.95% at 0% 67.51%, rgba(141, 102, 0, 0.85) 0%, rgba(32, 32, 32, 0.85) 100%);
    }
    
    #login-box {
        position: absolute;
        z-index: 0;
        top: 0px;
        left: 50%;
        height: 100%;
        width: 50%;
        background-color: var(--tertiary);
    }

    #login {
        position: absolute;
        top: 24vh;
        left: 80%;
        transform: translate(-80%, 0);
    }

    #login h1 {
        width: fit-content;
        color: #ffffff;
        font-size: 36px;
        font-weight: 300;
        border-bottom: 3px solid var(--secondary);
        margin-bottom: 6vh;
    }

    #login form {
        margin-left: 12%;
    }

    #login form label {
        color: var(--on-tertiary);
        font-family: Arial;
    }

    #login form input {
        width: 30vw;
        margin-bottom: 26px;
        padding: 5px 5px 5px 5px;
        color: var(--on-primary);
        background-color: var(--primary);
        border: var(--primary) 1px solid;
        border-radius: 5px;
        font-size: 14px;
    }

    #login form input:focus {
        outline: none;
        border: var(--secondary) 1px solid;
    }

    #login form p {
        position: relative;
        margin-top: 3vh;
        right: 30%;
        color: var(--on-tertiary);
        transform: translate(50%, 0);
    }

    #login form p a {
        color: var(--on-tertiary);
        transition: 0.15s;
    }

    #login form p a:hover {
        color: var(--secondary);
    }

    #login form div {
        position: relative;
        right: 28%;
        margin-top: -2vh;
        transform: translate(50%, 0);
    }

    #login form button {
        width: 110px;
        height: 32px;
        color: var(--on-secondary);
        background-color: var(--secondary);
        border: none;
        border-radius: 5px;
        font-size: 14px;
        transition: 0.15s;
    }

    #back-button {
        padding: 8px 40px 8px 40px;
        margin-right: 3vw;
        color: var(--on-primary);
        background-color: var(--tertiary);
        border: var(--on-primary) 1px solid;
        border-radius: 5px;
        font-size: 14px;
        transition: 0.15s;
    }

    @media screen and (max-device-width: 800px){
        #login-box {
            left: 0%;
            width: 100%;
        }

        #login {
            top: 12vh;
            left: 70vw;
            width: 75vw;
        }

        #login h1 {
            font-size: 26px;
        }

        #login form {
            margin-left: 6%;
        }

        #login form label {
            font-size: 14px;
        }

        #login form input {
            width: 65vw;
        }

        #login form p {
            max-width: 70%;
            margin-left: 7vw;
        }

        #login form div {
            width: max-content;
        }

        #login form button {
            width: 80px;
            height: 28px;
            font-size: 12px;
        }

        #back-button {
            padding: 7px 26px 7px 26px;
            font-size: 12px;
        }
    }
</style>