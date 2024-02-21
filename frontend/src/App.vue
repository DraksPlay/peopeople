<template>
  <head>
    <title>Chat</title>
  </head>
  <div class="app">

    <ChatMessage
    />

  </div>

</template>

<script>
import ChatMessage from './components/ChatMessage.vue';

export default {
  name: 'App',
  components: {
    ChatMessage
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  color: #333333;
}

.app {
  display: flex;
  justify-content: center;
}
</style>
