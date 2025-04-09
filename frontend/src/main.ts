import "./assets/main.css"
import { createApp } from "vue"
import { createPinia } from "pinia"
import App from "./App.vue"
import router from "@/app/landing/routes.ts"
import Vueform from "@vueform/vueform"
import vueformConfig from "./../vueform.config"

const app = createApp(App)
const pinia = createPinia()

app.use(router)
app.use(pinia)
app.use(Vueform, vueformConfig)
app.mount("#app")
