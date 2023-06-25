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

<body>
    <div id="container">
        <section id="calendar">
            <p>Calendář</p>
        </section>

        <section id="todos">
            <p>To do list</p>
        </section>

        <section id="notes">
            <p>Poznámky</p>
        </section>

        <style>
            body, html {
                height: 100%;
                margin: 0;
                overflow: hidden;
            }
        </style>
    </div>
</body>

<style>
    #container {
        height: 100%;
        width: 100%;
        overflow-y: scroll;
        scroll-snap-type: y mandatory;
    }

    section {
        height: 100%;
        width: 100%;
        scroll-snap-align: start;
        display: flex;
    }
    
    #calendar {
        background-color: #ffcc00;
    }

    #todos {
        background-color: #00ccff;
    }

    #notes {
        background-color: #cc00cc;
    }
</style>