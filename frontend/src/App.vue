<template>
  <body>
    <Friends/>

    <User />
    <Chat />  
  </body>
</template>

<script>
import Friends from './components/Friends.vue'

import User from './components/chat/User.vue'
import Chat from './components/chat/Chat.vue'

export default {
  name: 'App',
  components: {
    Friends,
    User,
    Chat
  }
}
</script>

<style>

</style>
