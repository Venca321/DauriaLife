<script>
    // @ts-nocheck
    import translations from "./translations";

    export let data;
    const lang = data.lang
    const langset = translations[lang]

    var underlined_old = "";
    function reveal() {
        var reveals = document.querySelectorAll(".reveal");

        for (var i = 0; i < reveals.length; i++) {
            var windowHeight = window.innerHeight;
            var elementTop = reveals[i].getBoundingClientRect().top;
            var elementVisible = 512;

            if (elementTop < windowHeight - elementVisible) {
                var element = document.getElementById("navbar");
                if (element){
                    if (reveals[i].id == "main-text") {
                    element.style.background = "#09182500";
                    } else {
                    element.style.background = "#091825";
                    }
                    underlined_old = reveals[i].id;
                }
            }
        }
    }

    window.addEventListener("scroll", reveal);
</script>

<svelte:head>
    <title>DauriaLife</title>
    <meta name="author" content="DauriaLife" />
</svelte:head>

<header id="navbar">
    <a href="/{lang}"><img src="/images/DauriaLife.png" alt="DariaLife.png"></a>
    <div id="centered">
        <a href="/{lang}#project">{langset["about_project"]}</a>
        <a href="/{lang}#team">{langset["about_us"]}</a>
        <a href="/{lang}#contact">{langset["contact"]}</a>
    </div>
    <a id="lang-button">{lang.toUpperCase()}</a>
</header>

<div id="picture">
    <img src="/images/calendar.png" alt="calendar.png">
</div>

<span id="picture-box"></span>

<section id="main-text" class="reveal">
    <h1>{langset["slogan"]}</h1>
    <a id="login-button" href="/{lang}/auth/login">{langset["login"]}</a>
    <a id="register-button" href="/{lang}/auth/register">{langset["register"]}</a>
</section>

<section id="project" class="reveal">
    <h1>{langset["about_project"]}</h1>
</section>

<section id="team" class="reveal">
    <h1>{langset["about_us"]}</h1>
</section>

<section id="contact" class="reveal">
    <h1>{langset["contact"]}</h1>
</section>

<section id="end">
</section>

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

    #centered {
        position: absolute;
        left: 51%;
        transform: translate(-51%, 0);
    }

    #centered a {
        margin-right: 4vw;
    }

    #lang-button {
        position: absolute;
        left: 97%;
        transform: translate(-97%, 0);
    }
    
    #picture {
        position: absolute;
        top: 20vh;
        left: 50%;
        transform: translate(-50%, 0);
    }

    #picture img {
        width: 75vw;
        mask-image: linear-gradient(180deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 80%);
    }
    
    #picture-box {
        position: absolute;
        top: 0px;
        left: 0px;
        height: 110%;
        width: 100%;
        background: linear-gradient(180deg, rgba(0, 0, 0, 0.85) 0%, rgba(27, 20, 0, 0.85) 45.83%, rgba(117, 84, 0, 0.85) 86.46%, rgba(54, 54, 54, 0.85) 100%, rgba(50, 50, 50, 0.85) 100%);
    }

    #main-text {
        position: absolute;
        width: max-content;
        max-width: 55%;
        top: 27.5vh;
        left: 50%;
        transform: translate(-50%, 0);
        text-align: center;
    }

    #main-text h1 {
        font-size: 48px;
        color: #ffffff;
        margin-bottom: 5vh;
        border-bottom: none;
    }

    #main-text a {
        padding: 10px;
        color: #ffffff;
        text-decoration: none;
        border: #ffffff 1px solid;
        border-radius: 5px;
        transition: 0.2s;
    }

    #main-text a:hover {
        background-color: #ffffff;
        color: #000000;
    }

    #login-button {
        margin-right: 1.5vw;
    }

    #register-button {
        margin-left: 1.5vw;
    }

    section h1 {
        font-size: 48px;
        color: #ffffff;
        margin-bottom: 5vh;
        border-bottom: var(--secondary) 1px solid;
    }

    #project {
        scroll-margin-top: 10vh;
        position: absolute;
        top: 125vh;
        left: 10%;
    }

    #team {
        scroll-margin-top: 10vh;
        position: absolute;
        top: 225vh;
        left: 10%;
    }

    #contact {
        scroll-margin-top: 10vh;
        position: absolute;
        top: 325vh;
        left: 10%;
    }

    #end {
        position: absolute;
        top: 425vh;
        left: 0;
        width: 100%;
        height: 20vh;
        background-color: var(--tertiary);
    }
</style>