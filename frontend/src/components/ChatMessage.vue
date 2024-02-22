<template>
    <div class="chat">
        
        <ChatList
        :messages="messages"
        :username="username"
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
                messages: [],
                username: null
            }
        },
        created() {
            const self = this;
            this.socket = new WebSocket("ws://localhost:8001/chat");

            this.socket.onopen = function() {
               var obj = {
                    "event": "open",
                    "body": {}
                }
                var json = JSON.stringify(obj);
                self.socket.send(json)
            }
            
            this.socket.onmessage = function(event) {
                var obj = JSON.parse(event.data);
                console.log(obj)
                if (obj.event == "messages") {
                    obj.body.messages.forEach((value) => {
                        self.messages.push({text: value.text, username: value.username})
                    })
                } else if (obj.event == "open") {
                    self.username = obj.body.username
                }
            }
            
        },
        methods: {
            sendMessage(message) {
                var new_message = {
                    text: message.text,
                    username: this.username
                }
                this.messages.push(new_message);
                var obj = {
                    "event": "new_message",
                    "body": {
                        "text": new_message.text,
                        "username": new_message.username
                    }
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