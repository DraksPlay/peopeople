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
                messages: []
            }
        },
        created() {
            const self = this;
            this.socket = new WebSocket("ws://localhost:8001/chat");
            
            this.socket.onmessage = function(event) {
                var obj = JSON.parse(event.data);
                obj.forEach((value) => {
                    self.messages.push({text: value.text})
                })
                
            }
            
        },
        methods: {
            sendMessage(message) {
                this.messages.push(message);
                var obj = {
                    text: message.text,
                }
                var json = JSON.stringify(obj);
                this.socket.send(json);
        }
    }
  }
</script>

<style scoped>
.chat {
    border: solid 2px #333333;
    border-radius: 10px;
    padding: 10px;
    margin-top: 30px;
    width: 50%;
    height: 50%;
}
</style>