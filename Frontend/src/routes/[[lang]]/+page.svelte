<script>
    // @ts-nocheck
    import Navbar from "$lib/Navbar.svelte";
    import { browser } from '$app/environment'
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

    if (browser) {
        window.addEventListener("scroll", reveal);
    }
</script>

<svelte:head>
    <title>DauriaLife</title>
    <meta name="author" content="DauriaLife" />
</svelte:head>

<Navbar lang={lang} langset={langset}/>

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
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus?</p>
</section>

<section id="team" class="reveal">
    <h1>{langset["about_us"]}</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus?</p>
</section>

<section id="contact" class="reveal">
    <h1>{langset["contact"]}</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus? Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Deserunt non, sapiente reiciendis debitis 
        laudantium odit animi molestias! Illo tempore natus laudantium est voluptatem, laboriosam, blanditiis 
        ducimus facilis, reprehenderit laborum delectus?</p>
</section>

<section id="end">
    <h2>Václav Parma 2023</h2>
</section>

<style>
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
        top: 30vh;
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
        width: fit-content;
        font-size: 48px;
        color: #ffffff;
        margin-bottom: 5vh;
        border-bottom: var(--secondary) 1px solid;
    }

    p {
        color: var(--on-primary);
        margin-left: 10%;
    }

    #project {
        scroll-margin-top: 10vh;
        max-width: 70%;
        position: absolute;
        top: 125vh;
        left: 10%;
    }

    #team {
        scroll-margin-top: 10vh;
        max-width: 70%;
        position: absolute;
        top: 200vh;
        left: 10%;
    }

    #contact {
        scroll-margin-top: 10vh;
        max-width: 70%;
        position: absolute;
        top: 275vh;
        left: 10%;
    }

    #end {
        position: absolute;
        text-align: center;
        top: 350vh;
        left: 0;
        width: 100%;
        height: 20vh;
        background-color: var(--tertiary);
    }

    #end h2 {
        margin-top: 8vh;
        color: var(--on-tertiary);
    }

    @media screen and (max-device-width: 800px){
        #main-text {
            max-width: 80%;
        }

        #main-text h1 {
            font-size: 26px;
        }

        section h1 {
            font-size: 26px;
        }

        p {
            font-size: 15px;
        }

        #project {
            top: 125vh;
        }

        #team {
            top: 300vh;
        }

        #contact {
            top: 475vh;
        }

        #end {
            top: 650vh;
        }

        #end h2 {
            font-size: 18px;
        }
    }
</style>