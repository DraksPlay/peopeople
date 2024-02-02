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
                socket: null,
                messages: [
                    {text: "test message"},
                    {text: "hello"}
            ]
            }
        },
        created() {
            this.socket = new WebSocket("ws://localhost:8001/chat");
            this.socket.onmessage = function(event) {
                console.log(event);
            }
            
        },
        methods: {
            sendMessage(message) {
                this.messages.push(message);
                this.socket.send(message);
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