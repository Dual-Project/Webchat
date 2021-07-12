<template>
    <div class="Input">
        <ul>
            <li><input type="text" name="msg" id="msg" placeholder="Insira a sua mensagem..."></li>
            <li><button><i class="fas fa-paper-plane"></i></button></li>
        </ul>       
    </div>
</template>

<script>
export default {
    name: 'Input',

}

</script>

<style scoped>

div{
width: 100%;
}

input[type=text]{
width: 100%;
height: 2em;
border: none;
}

ul li{
display: inline-block;
padding: 0;
}

button{
background: #5C258D;
border: none;
color: #FFF;
width: 200%;
border-bottom-left-radius: 0;
border-bottom-right-radius: 10px;
border-top-left-radius: 0;
border-top-right-radius: 10px;
}
</style>