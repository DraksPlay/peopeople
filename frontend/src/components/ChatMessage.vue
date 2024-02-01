<template>
    <div class="chat">
        
        <ChatList
        :messages="messages"
        />

        <ChatForm
        @send="sendMessage"
        />
    </div>
</template>

<script>
    import ChatList from './ChatList.vue';
    import ChatForm from './ChatForm.vue';
    export default {
        components: {
            ChatList,
            ChatForm
        },
        data() {
            return {
                messages: [
                    {text: "test message"},
                    {text: "hello"}
            ]
            }
        },
        methods: {
            sendMessage(message) {
                this.messages.push(message)
        }
    }
  }
</script>

<style scoped>
.chat {
    border: solid 2px #FF9400;
    border-radius: 10px;
    padding: 10px;
    margin-top: 30px;
    width: 50%;
    height: 50%;
}
</style>