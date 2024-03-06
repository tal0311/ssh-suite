const { createApp, ref } = Vue
import ell from '/eel.js'


const options = {
   template: `
          <section class="container">
            <section class="header-container"></section>
            <section class="logo"></section>
            <section class="file-list"></section>
            <section class="dashboard"></section>
            <section class="folder-details"></section>
            <section class="upload-file"></section>
            <section class="history"></section>
            <section class="terminal"></section>
            <section class="send-mail"></section>
          </section>
    
    `,
    data() {
        return{
            message: 'Hello Vue 3'

        }
    },
    methods: {},
    computed: {},
    watch: {},
    

}
const app= createApp(options)
app.mount('#app')