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
    border: 2px solid#333333;
    border-radius: 10px 0 0 10px;
    padding: 10px;
    width: 80%;
}

button {
    width: 20%;
    border-radius: 0 10px 10px 0;
    border: solid #333333;
    border-width: 2px 2px 2px 0;
    background: white;
}

button:hover {
    background: #333333;
    color: white;
}
</style>