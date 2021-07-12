<template>
  <section class="friends">
        <ul>
            <li>
                <ul>
                    <li><img src="../assets/festa.jpg"></li>
                    <br>
                    <li>Carlos Amaral</li>
                </ul>
                

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

<style scoped>
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

section.friends{
    background: var(--dark);
    height: auto;
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
    padding: 0.4em;
    margin-left: 0.5em;
    overflow: visible;
}

ul li:first-child{
    margin-left: 3em;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
}

ul li img{
    width: 50px;
    height: 50px;
}

</style>