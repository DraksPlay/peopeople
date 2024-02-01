<template>
    <div class="chat_form">

        <form @submit.prevent>
            <input
                v-model="message.text" 
                type="text"
                placeholder="Input message..."
            >
            <button
                @click="sendMessage"
            >Send</button>
        </form>

    </div>
</template>

<script>
    export default {
        name: "ChatForm",
        data() {
            return {
                message: {
                    text: ""
                }
            }
        },
        methods: {
            sendMessage() {
                this.$emit("send", this.message)
                this.message = {
                    text: ""
                }
            }
        }
    }
</script>

<style scoped>

.chat_form {
    margin-top: 10px;
}

form {
    display: flex;
    justify-content: space-between;
}

input {
    border: 2px solid#FF9400;
    border-radius: 10px;
    padding: 10px;
    width: 75%;
}

button {
    width: 23%;
    border-radius: 10px;
    border: 2px solid #FF9400;
    background: white;
}

button:hover {
    background: #FF9400;
    color: white;
}
</style>