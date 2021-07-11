<template>
  <section>
        <ul>
            <li>
                <img src="../assets/logo.png">
            </li>
            <li>
                <img src="../assets/logo.png">
            </li>
            <li>
                <img src="../assets/logo.png">
            </li>
            <li>
                <img src="../assets/logo.png">
            </li>
            <li>
                <img src="../assets/logo.png">
            </li>
            <li>
                <img src="../assets/logo.png">
            </li>
            <li>
                <img src="../assets/logo.png">
            </li>
            <li>
                <img src="../assets/logo.png">
            </li>
            <li>
                <img src="../assets/logo.png">
            </li>
            <li>
                <img src="../assets/logo.png">
            </li>
            <li>
                <img src="../assets/logo.png">
            </li>
            <li>
                <img src="../assets/logo.png">
            </li>
        </ul>
  </section>
</template>

<script>
export default {
    name: 'Friends'

}
</script>

<style>
:root{
    --light: #fff;
    --dark: #242424;
    --primary: #f93;

    --radius: 15px;
}

*{
    margin: 0;
    padding: 0;
}

section{
    background: var(--dark);
    height: 9vh;
    display: block;
    position: relative;
}

ul{
    padding-top: 0.5vh;
}

ul li{
    display: inline-block;
    background: var(--light);
    border-radius: var(--radius);
    padding: 1em;
    margin-left: 0.5em;
    overflow: visible;
}

ul li:first-child{
    margin-left: 3em;
}

ul li img{
    width: 1.5em;
    height: auto;
}

</style>