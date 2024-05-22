window.__VUE_PROD_HYDRATION_MISMATCH_DETAILS__ = true;

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from "./store";

const app = createApp(App);

app.use(router);
app.use(store);

app.mount('#app')
