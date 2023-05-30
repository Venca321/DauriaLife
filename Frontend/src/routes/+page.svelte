
<body>
    <div id="container">
        <section id="dashboard">
            <p>Dashboard</p>
        </section>

        <section id="automation">
            <p>Automatizace</p>
        </section>

        <section id="control">
            <p>Test</p>
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
    
    #dashboard {
        background-color: #ffcc00;
    }

    #automation {
        background-color: #00ccff;
    }

    #control {
        background-color: #cc00cc;
    }
</style>