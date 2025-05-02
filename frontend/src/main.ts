import "./assets/main.css"
import { createApp } from "vue"
import { createPinia } from "pinia"
import App from "./App.vue"
import router from "@/app/landing/routes.ts"
import Vueform from "@vueform/vueform"
import vueformConfig from "./../vueform.config"
import {useAuthStore} from "./common/stores/useAuthStore";

const app = createApp(App)
const pinia = createPinia()

app.use(router)
app.use(pinia)
app.use(Vueform, vueformConfig)

const authStore = useAuthStore()
authStore.init()

app.mount("#app")
