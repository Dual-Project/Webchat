<template>
<!DOCTYPE html>
<html lang="en">
<body>
  <Header />
  <div class="chat">
    <User username="João"/>
    <Chat />
    <Input />
  </div>
</body>
</html>
</template>

<script>
import User from './components/chat/User.vue'
import Chat from './components/chat/Chat.vue'
import Input from './components/chat/Input.vue'
import Header from './components/Header.vue'


export default {
  name: 'App',
  components: {
    Header,
    User,
    Chat,
    Input
  }
}
</script>

<style>
:root{
  --light: #fff;
  --dark: #242424;
  --radius: 15px;
}

*{
  font-family: 'Poppins';
}

body{
  background-image: linear-gradient(to right, #5C258D, #4389A2);
}

div.chat{
  background: var(--light);
  border-bottom-right-radius: var(--radius);
  border-bottom-left-radius: var(--radius);
  border-top-right-radius: var(--radius);
  border-top-left-radius: var(--radius);
  margin-top: 0em;
  margin-bottom: 3em;
  margin-left: 3em;
  margin-right: 3em;
  padding: 1em;
}

</style>
