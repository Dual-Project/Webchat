<template>
  <section class="chat">
    <div class="msg-amigo">
        <h5>Mensagem</h5>
    </div>


    <div class="msg-usuario">
        <h5>Eai</h5>
    </div>


    <div class="msg-amigo">
        <h5>Mensagem</h5>
    </div>


    <div class="msg-usuario">
        <h5>Eai</h5>
    </div>


    <div class="msg-amigo">
        <h5>Mensagem</h5>
    </div>


    <div class="msg-usuario">
        <h5>Eai</h5>
    </div>


    <div class="msg-amigo">
        <h5>Mensagem</h5>
    </div>


    <div class="msg-usuario">
        <h5>Eai</h5>
    </div>


    <div class="msg-amigo">
        <h5>Mensagem</h5>
    </div>


    <div class="msg-usuario">
        <h5>Eai</h5>
    </div>


    <div class="msg-amigo">
        <h5>Mensagem</h5>
    </div>


    <div class="msg-usuario">
        <h5>Eai</h5>
    </div>


    <div class="msg-amigo">
        <h5>Mensagem</h5>
    </div>


    <div class="msg-usuario">
        <h5>Eai</h5>
    </div>


    <div class="msg-amigo">
        <h5>Mensagem</h5>
    </div>


    <div class="msg-usuario">
        <h5>Eai</h5>
    </div>
  </section>
</template>




<script>
export default {
    name: 'Chat'
}
</script>




<style scoped>
:root{
    --light: #fff;
    --dark: #242424;
    --radius: 2px;
}

*{
    margin: 0;
    padding: 0;
    font-family: var(--teste);
}

section.chat{
    background: #e4e4e4;
    padding: 1em;
    margin-top: 1em;
    height: 70vh;
    border-top-right-radius: var(--radius);
    border-top-left-radius: var(--radius);
}

.msg-usuario{
    float: right;
    margin-top: 0.5em;
}
.msg-usuario h5{
    color: var(--dark);
    font-weight: 400;
}

.msg-amigo{
    width: 100%;
    float: left;
}
.msg-amigo h5{
    color: var(--dark);
    font-weight: 400;
}


</style>