<script>
    import Navbar from "$lib/Navbar.svelte";
    import translations from "./translations";

    export let data;
    const lang = data.lang
    // @ts-ignore
    const langset = translations[lang]
</script>

<svelte:head>
    <title>{langset["title"]}</title>
    <meta name="author" content="DauriaLife" />
</svelte:head>

<Navbar lang={lang} langset={langset} location="/auth/register"/>

<div id="picture">
    <img src="/images/calendar.png" alt="calendar.png">
</div>

<span id="picture-box"></span>
<span id="register-box"></span>

<div id="register">
    <h1>{langset["title"]}</h1>
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
        <div>
            <a id="back-button" href="/{lang}">{langset["back"]}</a>
            <button type="submit">{langset["register"]}</button>
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
    
    #register-box {
        position: absolute;
        z-index: 0;
        top: 0px;
        left: 50%;
        height: 100%;
        width: 50%;
        background-color: var(--tertiary);
    }

    #register {
        position: absolute;
        top: 12vh;
        left: 80%;
        transform: translate(-80%, 0);
    }

    #register h1 {
        width: fit-content;
        color: #ffffff;
        font-size: 36px;
        font-weight: 300;
        border-bottom: 3px solid var(--secondary);
        margin-bottom: 6vh;
    }

    #register form {
        margin-left: 12%;
    }

    #register form label {
        color: var(--on-tertiary);
        font-family: Arial;
    }

    #register form input {
        width: 30vw;
        margin-bottom: 16px;
        padding: 5px 5px 5px 5px;
        color: var(--on-primary);
        background-color: var(--primary);
        border: var(--primary) 1px solid;
        border-radius: 5px;
        font-size: 14px;
    }

    #register form input:focus {
        outline: none;
        border: var(--secondary) 1px solid;
    }

    #register form p {
        position: relative;
        color: var(--on-tertiary);
        margin-left: auto;
        margin-right: auto;
    }

    #register form p a {
        color: var(--on-tertiary);
        transition: 0.15s;
    }

    #register form p a:hover {
        color: var(--secondary);
    }

    #register form div {
        position: relative;
        margin-top: -2vh;
        margin-left: auto;
        margin-right: auto;
    }

    #register form button {
        width: 110px;
        height: 32px;
        margin-left: 1.5vw;
        color: var(--on-secondary);
        background-color: var(--secondary);
        border: none;
        border-radius: 5px;
        font-size: 14px;
        transition: 0.15s;
    }

    #back-button {
        padding: 8px 40px 8px 40px;
        color: var(--on-primary);
        background-color: var(--tertiary);
        border: var(--on-primary) 1px solid;
        border-radius: 5px;
        font-size: 14px;
        transition: 0.15s;
    }

    @media screen and (max-device-width: 800px){
        #register-box {
            left: 0%;
            width: 100%;
        }

        #register {
            top: 8vh;
            left: 70vw;
            width: 75vw;
        }

        #register h1 {
            font-size: 26px;
            margin-bottom: 4vh;
        }

        #register form {
            margin-left: 6%;
        }

        #register form label {
            font-size: 14px;
        }

        #register form input {
            width: 65vw;
            margin-bottom: 12px;
        }

        #register form p {
            max-width: 75%;
        }

        #register form div {
            width: max-content;
        }

        #register form button {
            width: 84px;
            height: 28px;
            font-size: 12px;
        }

        #back-button {
            padding: 7px 28px 7px 28px;
            font-size: 12px;
        }
    }
</style>