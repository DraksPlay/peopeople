<template>
    <div class="chat_list" v-scroll_down>
        
        <div class="message" v-for="(message, index) in messages" :key="index">
            <div class="message_content" v-if="this.username == message.username" style="justify-self: flex-end;">
                {{ message.text }}
            </div>
            <div class="message_content" v-else>
                {{ message.text }}
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        name: "ChatList",  
        props: {
            messages: {
                type: Array,
                required: true
            },
            username: {
                type: String,
                required: true
            }
        }
    }
</script>

<style scoped>
.chat_list {
    border: 2px solid #333333;
    border-radius: 10px;
    padding: 10px;
    overflow-y: scroll;
    overflow-x: hidden;
    word-wrap: break-word;
    height: 70vh;
}

.message {
    margin-top: 10px;
    display: grid;
}

.message_content {
    background-color: lightgray;
    width: 50%;
    border-radius: 10px;
    padding: 10px;
}
</style>